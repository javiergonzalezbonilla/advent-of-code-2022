import os
import math
import pdb
from typing import List
from solutions.utils import ReadFile
from solutions.day_11.utils import create_monkeys, Monkey


def get_monkey_business(monkeys: List[Monkey], rounds=20, divisor=3):
    lcm = math.lcm(*[monkey.test for monkey in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                new_item_value = monkey.evaluate_operation(item)
                new_item_value = new_item_value % lcm

                if divisor > 1:
                    new_item_value = math.floor(new_item_value / divisor)

                if new_item_value % monkey.test == 0:
                    monkeys[monkey.monkey_truthy_test_case].items.append(new_item_value)
                else:
                    monkeys[monkey.monkey_falsy_test_case].items.append(new_item_value)

            monkey.inspected_items += len(monkey.items)
            monkey.items = []

    inspected_items_per_monkey = [monkey.inspected_items for monkey in monkeys]
    inspected_items = inspected_items_per_monkey.copy()
    print(f"inspected_items_per_monkey {inspected_items_per_monkey}")
    max_1 = max(inspected_items_per_monkey)
    inspected_items_per_monkey.pop(inspected_items_per_monkey.index(max_1))
    max_2 = max(inspected_items_per_monkey)
    return max_1 * max_2, inspected_items


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    monkeys_description = ReadFile(dir_path + "/input.txt").get_data_from_line()
    monkeys = create_monkeys(monkeys_description)
    monkey_business, _ = get_monkey_business(monkeys, 20)
    print(f"Monkey business Part 1: {monkey_business}")

    monkeys = create_monkeys(monkeys_description)
    monkey_business, _ = get_monkey_business(monkeys, 10000, 1)
    print(f"Monkey business Part 2: {monkey_business}")
