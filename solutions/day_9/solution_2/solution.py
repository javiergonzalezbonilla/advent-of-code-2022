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
    if current_distance >= 0.1 + 2 ** 0.5:
        return True
    return False


def euclidean_distance(head, tail):
    return np.linalg.norm(np.array(head) - np.array(tail))


def update_head_position(position, direction):
    position = [pos + offset for pos, offset in zip(position, direction)]
    return position


def update_tail_position(head, tail):

    x_difference = head[0] - tail[0]
    y_difference = head[1] - tail[1]
    if x_difference and not y_difference:
        tail[0] += x_difference - np.sign(x_difference)
        return tail

    if not x_difference and y_difference:
        tail[1] += y_difference - np.sign(y_difference)
        return tail
    if x_difference and y_difference:
        if abs(x_difference) > abs(y_difference):
            tail[1] = head[1]
            tail[0] += x_difference - np.sign(x_difference)
        elif abs(y_difference) > abs(x_difference):
            tail[0] = head[0]
            tail[1] += y_difference - np.sign(y_difference)
        else:
            tail[0] += x_difference - np.sign(x_difference)
            tail[1] += y_difference - np.sign(y_difference)

    return tail


def get_tail_positions(movements):

    all_tail_positions = set()
    rope = [[0, 0] for _ in range(10)]
    all_tail_positions.add(tuple(rope[-1]))
    for direction, steps in movements:
        direction = directions_map[direction]
        rope = update_rope(all_tail_positions, rope.copy(), direction, steps)

    tails_positions_count = len(all_tail_positions)
    print(f"Tail position counts {tails_positions_count}")
    return all_tail_positions


def update_rope(all_tail_positions, rope, direction, steps):
    for _ in range(int(steps)):
        for index in range(len(rope)):
            if index == 0:
                rope[0] = update_head_position(rope[0], direction)
            else:
                head = rope[index - 1]
                tail = rope[index]
                if is_not_head_tail_valid_position(head, tail):
                    new_tail = update_tail_position(head.copy(), tail.copy())
                    rope[index] = new_tail.copy()
                else:
                    break
        all_tail_positions.add(tuple(rope[-1]))
    return rope


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    movements = ReadFile(dir_path + "/input.txt").get_data_from_raw_table()
    get_tail_positions(movements)
