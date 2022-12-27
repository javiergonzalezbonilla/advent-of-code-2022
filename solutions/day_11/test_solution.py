import os
import unittest
from solutions.utils import ReadFile
from solutions.day_11.solution import create_monkeys, get_monkey_business


class MonkeysBusinessTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        monkeys_description = ReadFile(
            dir_path + "/sample_input.txt"
        ).get_data_from_line()
        self.monkeys = create_monkeys(monkeys_description)
        assert len(self.monkeys) == 4
        return super().setUp()

    def test_monkeys(self):
        monkey_busines, inspected_items = get_monkey_business(self.monkeys, 20)
        assert monkey_busines == 10605

    def test_monkeys_part2_1(self):
        monkey_busines, inspected_items = get_monkey_business(self.monkeys, 1, 1)
        assert inspected_items == [2, 4, 3, 6]

    def test_monkeys_part2_20(self):
        monkey_busines, inspected_items = get_monkey_business(self.monkeys, 20, 1)
        assert inspected_items == [99, 97, 8, 103]

    def test_monkeys_part2_10000(self):
        monkey_busines, inspected_items = get_monkey_business(self.monkeys, 10000, 1)
        assert inspected_items == [52166, 47830, 1938, 52013]
        assert monkey_busines == 2713310158
