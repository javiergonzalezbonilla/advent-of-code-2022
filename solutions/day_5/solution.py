import os

from solutions import utils


class Stack:
    def __init__(self, stack=[], size=None):
        self.stack = stack
        self.size = size

    def get_size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def pop(self):
        if self.stack.is_empty():
            raise Exception("Empty stack")
        return self.stack.pop()

    def push(self, value):
        if self.size and self.get_size() > self.size:
            raise Exception("Stack overflow")
        self.stack.append(value)

    def remove_n(self, n):
        to_remove = self.stack[-n:]
        self.stack = self.stack[:-n]
        return to_remove

    def add_n(self, values):
        self.stack.extend(values)

    def view_top(self):
        return self.stack[-1]


def solution(stacks_data, movements_data, multiple_crates=False):

    stacks = [Stack(stack=[*stack_data][::-1]) for stack_data in stacks_data]

    for movement in movements_data:
        [crates_count, from_stack_index, to_stack_index] = [
            int(data) for data in movement.split(",")
        ]

        from_stack = stacks[from_stack_index - 1]
        to_stack = stacks[to_stack_index - 1]

        if multiple_crates:
            crates = from_stack.remove_n(crates_count)
            to_stack.add_n(crates)
        else:
            for _ in range(crates_count):
                crate = from_stack.pop()
                to_stack.push(crate)

    top = "".join([stack.view_top() for stack in stacks])
    print(f"Top elements on stacks: {top}")


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    stacks_data = utils.ReadFile(dir_path + "/inputs/stacks.txt").get_data_from_line()
    movements_data = utils.ReadFile(
        dir_path + "/inputs/movements.txt"
    ).get_data_from_line()
    solution(stacks_data, movements_data)
    solution(stacks_data, movements_data, True)
