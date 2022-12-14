
import unittest
from solutions.day_9.solution_2 import solution


class SolutionTwoTestSuite(unittest.TestCase):
    def test_update_tail_position(self):

        heads = [
            [5, 2],
            [5, 1],
            [4, 1],
            [3, 1],
            [2, 1],
            [5, 3],
            [3, 3],
            [5, 3],
        ]
        tails = [
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
            [4, 1],
            [1, 1],
            [5, 1],
        ]
        results = [[5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [5, 2], [2, 2], [5, 2]]
        for head, tail, expected in zip(heads, tails, results):
            result = solution.update_tail_position(head, tail)
            assert expected == result

    def test_update_rope_R5(self):
        rope = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
        ]
        expected_rope = [
            [5, 0],
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
        ]
        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[1, 0], steps=5
        )
        assert expected_rope == result

    def test_update_rope_U8(self):
        rope = [
            [5, 0],
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
        ]
        expected_rope = [
            [5, 8],
            [5, 7],
            [5, 6],
            [5, 5],
            [5, 4],
            [4, 4],
            [3, 3],
            [2, 2],
            [1, 1],
            [0, 0],
        ]
        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[0, 1], steps=8
        )
        assert expected_rope == result

    def test_update_rope_L8(self):
        rope = [
            [5, 8],
            [5, 7],
            [5, 6],
            [5, 5],
            [5, 4],
            [4, 4],
            [3, 3],
            [2, 2],
            [1, 1],
            [0, 0],
        ]

        expected_rope = [
            [-3, 8],
            [-2, 8],
            [-1, 8],
            [0, 8],
            [1, 8],
            [1, 7],
            [1, 6],
            [1, 5],
            [1, 4],
            [1, 3],
        ]

        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[-1, 0], steps=8
        )
        assert expected_rope == result

    def test_update_rope_D3(self):
        rope = [
            [-3, 8],
            [-2, 8],
            [-1, 8],
            [0, 8],
            [1, 8],
            [1, 7],
            [1, 6],
            [1, 5],
            [1, 4],
            [1, 3],
        ]

        expected_rope = [
            [-3, 5],
            [-3, 6],
            [-2, 7],
            [-1, 7],
            [0, 7],
            [1, 7],
            [1, 6],
            [1, 5],
            [1, 4],
            [1, 3],
        ]

        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[0, -1], steps=3
        )
        assert expected_rope == result

    def test_update_rope_R17(self):
        rope = [
            [-3, 5],
            [-3, 6],
            [-2, 7],
            [-1, 7],
            [0, 7],
            [1, 7],
            [1, 6],
            [1, 5],
            [1, 4],
            [1, 3],
        ]

        expected_rope = [
            [14, 5],
            [13, 5],
            [12, 5],
            [11, 5],
            [10, 5],
            [9, 5],
            [8, 5],
            [7, 5],
            [6, 5],
            [5, 5],
        ]

        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[1, 0], steps=17
        )
        assert expected_rope == result

    def test_update_rope_D10(self):
        rope = [
            [14, 5],
            [13, 5],
            [12, 5],
            [11, 5],
            [10, 5],
            [9, 5],
            [8, 5],
            [7, 5],
            [6, 5],
            [5, 5],
        ]

        expected_rope = [
            [14, -5],
            [14, -4],
            [14, -3],
            [14, -2],
            [14, -1],
            [14, 0],
            [13, 0],
            [12, 0],
            [11, 0],
            [10, 0],
        ]

        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[0, -1], steps=10
        )
        assert expected_rope == result

    def test_update_rope_L25(self):
        rope = [
            [14, -5],
            [14, -4],
            [14, -3],
            [14, -2],
            [14, -1],
            [14, 0],
            [13, 0],
            [12, 0],
            [11, 0],
            [10, 0],
        ]

        expected_rope = [
            [-11, -5],
            [-10, -5],
            [-9, -5],
            [-8, -5],
            [-7, -5],
            [-6, -5],
            [-5, -5],
            [-4, -5],
            [-3, -5],
            [-2, -5],
        ]

        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[-1, 0], steps=25
        )
        assert expected_rope == result

    def test_update_rope_U20(self):
        rope = [
            [-11, -5],
            [-10, -5],
            [-9, -5],
            [-8, -5],
            [-7, -5],
            [-6, -5],
            [-5, -5],
            [-4, -5],
            [-3, -5],
            [-2, -5],
        ]

        expected_rope = [
            [-11, 15],
            [-11, 14],
            [-11, 13],
            [-11, 12],
            [-11, 11],
            [-11, 10],
            [-11, 9],
            [-11, 8],
            [-11, 7],
            [-11, 6],
        ]

        result = solution.update_rope(
            all_tail_positions=set(), rope=rope.copy(), direction=[0, 1], steps=20
        )
        assert expected_rope == result
