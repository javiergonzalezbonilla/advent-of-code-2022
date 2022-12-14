# -*- coding: utf-8 -*-
from unittest import TestCase

from solutions.day_9.solution_1 import solution


class TestDayNineSolutionSuite(TestCase):
    def test_valid_tail_position(self):
        head = [4, 1]
        tail = [3, 0]
        assert solution.is_not_head_tail_valid_position(head, tail) is False

    def test_update_tail_left_direction(self):
        tail = [2, 1]
        head = [0, 1]
        direction = [-1, 0]
        response = solution.update_tail_position(head, tail, direction)
        assert response == [1, 1]

    def test_update_tail_right_direction(self):
        tail = [0, 1]
        head = [3, 1]
        direction = [1, 0]
        response = solution.update_tail_position(head, tail, direction)
        assert response == [2, 1]

    def test_update_tail_up_direction(self):
        tail = [1, 1]
        head = [1, 3]
        direction = [0, 1]
        response = solution.update_tail_position(head, tail, direction)
        assert response == [1, 2]

    def test_update_tail_down_direction(self):
        tail = [3, 5]
        head = [3, 3]
        direction = [0, -1]
        response = solution.update_tail_position(head, tail, direction)
        assert response == [3, 4]

    def test_diagonal_positions_bottom_left(self):
        tail = [4, 3]
        head = [2, 2]
        direction = [-1, 0]
        response = solution.update_tail_position(head, tail, direction)
        assert response == [3, 2]

    def test_diagonal_positions_up_left(self):
        tail = [4, 3]
        head = [2, 4]
        direction = [-1, 0]
        response = solution.update_tail_position(head, tail, direction)
        assert response == [3, 4]


class TestGetTailsPosition(TestCase):
    def test_tails_positions(self):
        movements = [
            ["R", "4"],
            ["U", "4"],
            ["L", "3"],
            ["D", "1"],
            ["R", "4"],
            ["D", "1"],
            ["L", "5"],
            ["R", "2"],
        ]
        count = solution.get_tail_positions(movements)
        assert count == 13
