import os
from solutions.utils import ReadFile

WINDOW_LEN = 4


def are_not_different_characters(characters, window_len):
    return len(set([*characters])) != window_len


def get_start_of_datastream(signal, window_len):
    index = 0
    while are_not_different_characters(signal[index: index + window_len], window_len):
        index += 1
    return index + window_len


def solution(signals, window_len):
    for signal in signals:
        print(get_start_of_datastream(signal, window_len))


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    signals = ReadFile(dir_path + "/input.txt").get_data_from_line()
    print("###Solution 1###")
    solution(signals, 4)
    print("###Solution 2###")
    solution(signals, 14)
