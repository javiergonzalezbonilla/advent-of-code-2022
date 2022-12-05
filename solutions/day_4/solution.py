import os

from solutions import utils


def get_section_ranges(section_assignment):
    section_1, section_2 = section_assignment.split(",")
    return [int(value) for value in [*section_1.split("-"), *section_2.split("-")]]


def solution(section_assignments):
    fully_contained = 0
    with_overlap = 0
    for section_assignment in section_assignments:
        [s1_min, s1_max, s2_min, s2_max] = get_section_ranges(section_assignment)
        if (s1_min <= s2_min and s1_max >= s2_max) or (
            s2_min <= s1_min and s2_max >= s1_max
        ):
            fully_contained += 1
        if (s1_min <= s2_min and s1_max >= s2_min) or (
            s2_min <= s1_min and s2_max >= s1_min
        ):
            with_overlap += 1
    return fully_contained, with_overlap


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    section_assignments = utils.ReadFile(dir_path + "/input.txt").get_data_from_line()
    fully_contained, with_overlap = solution(section_assignments)
    print(f"Total fully contained sections: : {fully_contained}")
    print(f"Total overlapped sections: : {with_overlap}")
