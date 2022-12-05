# -*- coding: utf-8 -*-

import os

from solutions.utils import ReadFile


class TopNElments:
    def __init__(self, n):
        self.elements = []
        self.n = n

    def __repr__(self) -> str:
        top_elements_str = []
        for index, value in reversed(self.elements):
            top_elements_str.append(f"Index: {index}: Value {value} \n")
        return "".join(top_elements_str)

    def verify_element(self, element):
        if len(self.elements) < self.n:
            self.elements.append(element)
            self.elements.sort(key=lambda x: x[1])
        else:
            if element > self.elements[0]:
                self.elements[0] = element
                self.elements.sort(key=lambda x: x[1])

    @property
    def get_total_value(self):
        total_value = 0
        for index, value in self.elements:
            total_value += value
        return total_value


def solution(data):
    data_length = len(data)
    top_n_elements = TopNElments(3)

    def find_max(index=0, max_value=0, selected_index=0):
        if index == data_length:
            return max_value, selected_index
        else:
            cumulated_values = sum(data[index])
            if cumulated_values > max_value:
                max_value = cumulated_values
                selected_index = index
            top_n_elements.verify_element([index, cumulated_values])
            return find_max(index + 1, max_value, selected_index)

    my_max, selected_index = find_max()
    print(f"Max calories {my_max}: Elf index: {selected_index}", end="\n\n")
    print(top_n_elements)
    print(f"Total Top 3: {top_n_elements.get_total_value}")


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = ReadFile(dir_path + "/input.txt").get_data_separated_by_breakline()
    solution(data)
