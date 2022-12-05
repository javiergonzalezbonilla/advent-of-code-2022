import os
from functools import reduce

from solutions import utils


def solution(rucksacks):
    priorities_cum_sum = 0
    for rucksack in rucksacks:
        compartment_length = len(rucksack) // 2
        compartment_1 = set(rucksack[:compartment_length])
        compartment_2 = set(rucksack[compartment_length:])
        common = compartment_1.intersection(compartment_2).pop()
        priorities_cum_sum += find_priority(common)
    return priorities_cum_sum


def solution_2(rucksacks):
    rucksacks_triplets_count = len(rucksacks) // 3
    priorities_cum_sum = 0
    for triplet_index in range(rucksacks_triplets_count):
        triplet = rucksacks[triplet_index * 3 : (triplet_index + 1) * 3]
        common = reduce(lambda x, y: set(x) & set(y), triplet)
        priorities_cum_sum += find_priority(common.pop())
    return priorities_cum_sum


def find_priority(common):
    if common.islower():
        return ord(common) - 96
    else:
        return ord(common) - 65 + 27


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    rucksacks = utils.ReadFile(dir_path + "/input.txt").get_data_from_line()
    value = solution(rucksacks)
    print(f"Total Value: solution 1: {value}")
    value = solution_2(rucksacks)
    print(f"Total Value: solution 2: {value}")
