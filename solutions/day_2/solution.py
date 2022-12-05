# -*- coding: utf-8 -*-

import os

from solutions.utils import ReadFile

# Opponent A for Rock, B for Paper, and C for Scissors.
# Player X for Rock, Y for Paper, and Z for Scissors.

# Choice Points
# Rock 1
# Paper 2
# Scissors 3

# match points 0 if you lost, 3 if the round was a draw, and 6 if you won.

X = "A"
Y = "B"
Z = "C"

match_status_result_points = {
    "AA": 3,
    "AB": 6,
    "AC": 0,
    "BA": 0,
    "BB": 3,
    "BC": 6,
    "CA": 6,
    "CB": 0,
    "CC": 3,
}

choice_selection_points = {"A": 1, "B": 2, "C": 3}

# X LOSE
# Y Draw
# Z Win
game_result_map = {
    #   DRAW WIN LOSE
    "A": {"Y": "A", "Z": "B", "X": "C"},
    #   WIN DRAW LOSE
    "B": {"Z": "C", "Y": "B", "X": "A"},
    #   LOSE WIN DRAW
    "C": {"X": "B", "Z": "A", "Y": "C"},
}


def solution1(data):
    total_score = 0
    for opponent_choice, player_choice in data:
        player_choice = eval(player_choice)
        match_status = opponent_choice + player_choice
        total_score += (
            match_status_result_points[match_status]
            + choice_selection_points[player_choice]
        )
    print(f"Total: score {total_score}")


def solution2(data):
    total_score = 0
    for opponent_choice, expected_result in data:
        player_choice = game_result_map[opponent_choice][expected_result]
        total_score += (
            choice_selection_points[player_choice]
            + match_status_result_points[opponent_choice + player_choice]
        )
    print(f"Total: score {total_score}")


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data = ReadFile(dir_path + "/input.txt").get_data_from_raw_table()
    solution1(data)
    solution2(data)
