import os
from solutions.utils import ReadFile


class Task:
    def __init__(self, instruction, created_at):
        self.processing_time = 1
        self.instruction = instruction
        self.created_at = created_at
        self.execution_time = 0
        self.executed = False
        self._set_operation_time()

    def __repr__(self):
        return (
            f"{self.instruction} -- Executed: {self.executed} -- "
            "Created {self.created_at} -- "
            "Should be executed on cycle{self.execution_time} \n"
        )

    def _set_operation_time(self):
        if self.instruction == ["noop"]:
            self.execution_time = self.created_at + 1
        else:
            self.processing_time = 2
            self.execution_time = self.created_at + 2

    def update(self, current_cycle):
        if current_cycle == self.execution_time:
            self.executed = True
            return self.execute()
        return 0

    def execute(self):
        if self.instruction == ["noop"]:
            return 0
        else:
            return int(self.instruction[1])


class TaskExecution:
    def __init__(self, program):
        self.current_cycle = -1
        self.current_value = 1
        self.current_task = None
        self.values_on_cycles = []
        self.history = []
        self.program = program
        self.finished = False

    def execute_tasks(self):
        if self.current_task:
            self.current_value += self.current_task.update(self.current_cycle)
            if self.current_task.executed:
                self._process_task()
        else:
            self._process_task()
        self.values_on_cycles.append(self.current_value)
        self.history.append((self.current_task.instruction, self.current_value))

    def _process_task(self):
        try:
            instruction = self.program.pop()
            self.current_task = Task(instruction, self.current_cycle)
        except IndexError as e:
            self.finished = True

    def update(self):
        self.current_cycle += 1
        self.execute_tasks()
        if not self.program:
            self.finished = True


class RenderSprite:
    def __init__(self, values):
        self.values = values
        self.offset = 2
        self.size = 40

    def should_render_pixel(self, cycle, value):

        cycle = cycle % self.size

        lower_limit = value
        upper_limit = value + self.offset

        if cycle >= lower_limit and cycle <= upper_limit:
            return True
        return False

    def transform_values(self):
        pixels = []
        for index, value in enumerate(self.values):
            cycle = index + 1
            if self.should_render_pixel(cycle, value):
                pixels.append("#")
            else:
                pixels.append(".")
        return "".join(pixels)

    def render(self):
        lines_count = len(self.values) // self.size
        lines = []

        transformed_values = self.transform_values()
        for index in range(lines_count):
            print(transformed_values[index * self.size : (index + 1) * self.size])


def calculate_signal_strength(program):
    program.reverse()
    executing_tasks = TaskExecution(program[:])
    while not executing_tasks.finished:
        executing_tasks.update()

    cycles = [i for i in range(20, 221, 40)]
    signals = [executing_tasks.values_on_cycles[cycle - 1] * cycle for cycle in cycles]
    signal_strength = sum(signals)

    print(f"Signals {signals}")
    print(f"Signal Strength {signal_strength}")

    rs = RenderSprite(executing_tasks.values_on_cycles)
    rs.render()

    return signal_strength


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    program = ReadFile(dir_path + "/input.txt").get_data_from_raw_table()
    calculate_signal_strength(program)
