import os
from solutions import utils

def solution(rucksacks):
    priorities_cum_sum = 0
    for rucksack in rucksacks:
        compartment_length = len(rucksack) // 2
        compartment_1 = set(rucksack[:compartment_length])
        compartment_2 = set(rucksack[compartment_length:])
        common = compartment_1.intersection(compartment_2).pop()
        if common.islower():
            priorities_cum_sum += ord(common) - 96
        else:
            priorities_cum_sum += ord(common) - 65 + 27
    return priorities_cum_sum

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    rucksacks = utils.ReadFile(dir_path + "/input.txt").get_data_from_line()
    value = solution(rucksacks)
    print(f'Total Value {value}')

