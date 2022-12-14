import pdb
import unittest
from solutions.day_9.solution_2 import solution


class SolutionTwoTestSuite(unittest.TestCase):
    def test_update_tail_position(self):

        heads = [[5, 2], [5, 1], [4, 1], [3, 1], [2, 1], [5, 3], [3, 3]]
        tails = [
            [4, 0],
            [3, 0],
            [2, 0],
            [1, 0],
            [0, 0],
            [4, 1],
            [1, 1],
        ]
        results = [[5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [5, 2], [2, 2]]
        for head, tail, expected in zip(heads, tails, results):
            result = solution.update_tail_position(head, tail)
            assert expected == result

    def test_update_rope_1(self):
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

    def test_update_rope_2(self):
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
        pdb.set_trace()
        assert expected_rope == result

    # def test_update_rope_3(self):
    #     rope = [
    #         [5, 8],
    #         [5, 7],
    #         [5, 7],
    #         [5, 7],
    #         [5, 6],
    #         [5, 5],
    #         [4, 4],
    #         [3, 3],
    #         [2, 2],
    #         [1, 1],
    #     ]

    #     expected_rope = [
    #         [-3, 8],
    #         [-2, 8],
    #         [-1, 8],
    #         [0, 8],
    #         [1, 8],
    #         [1, 7],
    #         [1, 6],
    #         [1, 5],
    #         [1, 4],
    #         [1, 3],
    #     ]

        # result = solution.update_rope(
        #     all_tail_positions=set(), rope=rope.copy(), direction=[-1, 0], steps=8
        # )
        # pdb.set_trace()
        # assert expected_rope == result

