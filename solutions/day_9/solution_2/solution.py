import os
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
    if x_difference and not y_difference:
        tail[0] += x_difference - direction[0]
        return tail

    if not x_difference and y_difference:
        tail[1] += y_difference - direction[1]
        return tail

    if x_difference and y_difference:
        if abs(x_difference) > abs(y_difference):
            tail[1] = head[1]
            tail[0] += x_difference - direction[0]
        else:
            tail[0] = head[0]
            tail[1] += y_difference - direction[1]
    return tail


def get_tail_positions(movements):

    all_tail_positions = set()
    rope = [[0, 0] for _ in range(10)]
    all_tail_positions.add(tuple(rope[-1]))
    for direction, steps in movements:
        direction = directions_map[direction]
        for _ in range(int(steps)):
            head = rope[0]
            head = update_head_position(head, direction)
            rope[0] = head
            ancestor = head
            for index, tail in enumerate(rope[1:]):
                if is_not_head_tail_valid_position(ancestor, tail):
                    tail = update_tail_position(ancestor, tail, direction)
                    rope[index + 1] = tail.copy()
                ancestor = tail.copy()
            all_tail_positions.add(tuple(rope[-1]))
    tails_positions_count = len(all_tail_positions)

    print(f"Tail position counts {tails_positions_count}")
    return tails_positions_count


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    movements = ReadFile(dir_path + "/sample_input.txt").get_data_from_raw_table()
    get_tail_positions(movements)
