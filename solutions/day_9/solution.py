import os
import pdb
import numpy as np
from solutions.utils import ReadFile

directions_map = {
    "R": [1, 0],
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
}


def is_not_head_tail_valid_position(head, tail):
    current_distance = euclidean_distance(head, tail)
    if current_distance >= 2:
        return True
    return False


def euclidean_distance(head, tail):
    return np.linalg.norm(np.array(head) - np.array(tail))


def update_head_position(position, direction):
    position = [pos + offset for pos, offset in zip(position, direction)]
    return position


def update_tail_position(head, tail, direction):

    x_difference = head[0] - tail[0]
    y_difference = head[1] - tail[1]

    # print(f"x diff: {abs(x_difference)}")
    # print(f"y diff: {abs(y_difference)}")

    # horizontal
    if x_difference and not y_difference:
        tail[0] += x_difference - direction[0]
        return tail

    if not x_difference and y_difference:
        tail[1] += y_difference - direction[1]
        return tail

    if x_difference and y_difference:
        if abs(x_difference) > abs(y_difference):
            print("x bigger")
            tail[1] = head[1]
            tail[0] += x_difference - direction[0]
        else:
            print("y bigger")
            tail[0] = head[0]
            tail[1] += y_difference - direction[1]
    return tail


def get_tail_positions(movements):

    all_tail_positions = set()
    origin = [0, 0]
    head = origin.copy()
    tail = origin.copy()
    all_tail_positions.add(tuple(tail))
    for direction, steps in movements:
        direction = directions_map[direction]
        for step in range(int(steps)):
            head = update_head_position(head, direction)
            if is_not_head_tail_valid_position(head, tail):
                tail = update_tail_position(head, tail, direction)
                all_tail_positions.add(tuple(tail))
    tails_positions_count = len(all_tail_positions)

    print(f"Tail position counts {tails_positions_count}")
    return tails_positions_count


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    movements = ReadFile(dir_path + "/input.txt").get_data_from_raw_table()
    get_tail_positions(movements)
