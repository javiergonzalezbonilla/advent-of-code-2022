import os
import unittest
from solutions.day_10.solution import (
    TaskExecution,
    Task,
    calculate_signal_strength,
    RenderSprite,
)
from solutions.utils import ReadFile


class TaskTestSuite(unittest.TestCase):
    def test_task_exists(self):
        task = Task(["noop"], 0)
        assert isinstance(task, Task)

    def test_operation_time_noop(self):
        task = Task(["noop"], 0)
        assert task.execution_time == 1

    def test_operation_time_add(self):
        task = Task(["addx", 3], 0)
        assert task.execution_time == 2

    def test_update_task_noop(self):
        task = Task(["noop"], 0)
        task.update(1)
        assert task.executed == True

    def test_update_task_noop(self):
        task = Task(["addx", 3], 0)
        task.update(2)
        assert task.executed == True


class TaskExecutionTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.program = [
            ["noop"],
            ["addx", "3"],
            ["addx", "-5"],
        ]

        self.program.reverse()  # reversed program

        self.te = TaskExecution(self.program)
        return super().setUp()

    def test_task_execution_exists(self):
        assert isinstance(self.te, TaskExecution)
        assert self.te.current_cycle == -1
        assert self.te.current_value == 1
        assert self.te.current_task == None
        assert self.te.values_on_cycles == []
        assert self.te.program == self.program

    def test_task_execution(self):

        assert self.te.finished is False

        self.te.update()
        assert self.te.current_cycle == 0
        assert self.te.current_task != None
        assert self.te.current_task.executed is False
        assert self.te.current_task.instruction == ["noop"]
        assert self.te.values_on_cycles == [1]

        self.te.update()
        assert self.te.current_cycle == 1
        assert self.te.current_task != None
        assert self.te.current_task.instruction == ["addx", "3"]
        assert self.te.values_on_cycles == [1, 1]

        self.te.update()
        assert self.te.current_cycle == 2
        assert self.te.current_task != None
        assert self.te.current_task.instruction == ["addx", "3"]
        assert self.te.values_on_cycles == [1, 1, 1]

        self.te.update()
        assert self.te.current_value == 4
        assert self.te.current_cycle == 3
        assert self.te.current_task != None
        assert self.te.current_task.instruction == ["addx", "-5"]
        assert self.te.values_on_cycles == [1, 1, 1, 4]

        self.te.update()
        assert self.te.current_value == 4
        assert self.te.current_cycle == 4
        assert self.te.current_task != None
        assert self.te.current_task.instruction == ["addx", "-5"]
        assert self.te.values_on_cycles == [1, 1, 1, 4, 4]

        self.te.update()
        assert self.te.current_value == -1
        assert self.te.current_cycle == 5
        assert self.te.current_task != None
        assert self.te.current_task.instruction == ["addx", "-5"]
        assert self.te.values_on_cycles == [1, 1, 1, 4, 4, -1]
        assert self.te.finished is True


class CalculateSignalStrength(unittest.TestCase):
    def test_calculate_signal_strength(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        program = ReadFile(dir_path + "/sample_input.txt").get_data_from_raw_table()
        signal_strength = calculate_signal_strength(program)
        assert signal_strength == 13140


class RenderSpriteTestSuite(unittest.TestCase):
    def test_render_pixel(self):
        rs = RenderSprite([])
        assert rs.should_render_pixel(cycle=1, value=1) is True
        assert rs.should_render_pixel(cycle=2, value=1) is True
        assert rs.should_render_pixel(cycle=3, value=1) is True
        assert rs.should_render_pixel(cycle=4, value=1) is False
        assert rs.should_render_pixel(cycle=4, value=5) is False

    def test_render_sprite(self):
        values = [
            1,
            1,
            16,
            16,
            5,
            5,
            11,
            11,
            8,
            8,
            13,
            13,
            12,
            12,
            4,
            4,
            17,
            17,
            21,
            21,
            21,
            20,
            20,
            25,
            25,
            24,
            24,
            29,
            29,
            28,
            28,
            33,
            33,
            32,
            32,
            37,
            37,
            36,
            36,
            1,
            1,
            2,
            2,
            26,
            26,
            7,
            7,
            8,
            8,
            24,
            24,
            13,
            13,
            13,
            13,
            34,
            34,
            19,
            19,
            19,
            19,
            16,
            16,
            25,
            25,
            26,
            26,
            23,
            23,
            31,
            31,
            32,
            32,
            37,
            37,
            37,
            37,
            37,
            37,
            37,
            1,
            1,
            1,
            2,
            2,
            9,
            9,
            9,
            9,
            9,
            11,
            11,
            17,
            17,
            17,
            17,
            17,
            17,
            17,
            18,
            18,
            18,
            18,
            25,
            25,
            26,
            26,
            26,
            13,
            13,
            26,
            26,
            33,
            33,
            33,
            34,
            34,
            1,
            1,
            1,
            1,
            1,
            3,
            3,
            3,
            3,
            3,
            11,
            11,
            11,
            10,
            10,
            12,
            12,
            13,
            13,
            13,
            30,
            30,
            21,
            21,
            22,
            22,
            23,
            23,
            20,
            20,
            31,
            31,
            31,
            31,
            32,
            32,
            32,
            33,
            33,
            33,
            33,
            20,
            20,
            1,
            1,
            2,
            2,
            5,
            5,
            31,
            31,
            1,
            1,
            13,
            13,
            12,
            12,
            15,
            15,
            16,
            16,
            16,
            16,
            16,
            7,
            7,
            25,
            25,
            26,
            26,
            28,
            28,
            28,
            28,
            37,
            37,
            37,
            37,
            37,
            36,
            36,
            38,
            38,
            1,
            1,
            2,
            2,
            5,
            5,
            5,
            20,
            20,
            -1,
            -1,
            21,
            21,
            15,
            15,
            16,
            16,
            16,
            18,
            18,
            19,
            19,
            19,
            9,
            9,
            9,
            9,
            29,
            29,
            30,
            30,
            32,
            32,
            34,
            34,
            28,
            28,
            17,
            17,
            17,
        ]
        expected_output = "##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###.#######.......#######.......#######....."

        rs = RenderSprite(values)
        pixels = rs.transform_values()
        assert pixels == expected_output
