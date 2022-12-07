import os
import pdb
from solutions.utils import ReadFile

MEMORY_MAP = dict()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File: {self.name} -- size: {self.size}"

LIMIT_SIZE = 100000

VALID_DIRECTORIES = set()


class Directory:
    def __init__(self, name, parent=None):
        self.directories = []
        self.files = []
        self.parent = parent
        self.name = name
        self.size = 0

    def __repr__(self) -> str:
        return f"Directory Name: {self.name}"

    def directory_exists(self, directory_name):
        directory_names = [str(directory) for directory in self.directories]
        return directory_name in directory_names

    def file_exists(self, file_name):
        files_names = [str(_file) for _file in self.files]
        return file_name in files_names

    def insert_directory(self, directory_name):
        if not self.directory_exists(directory_name):
            directory = Directory(directory_name, parent=self)
            self.directories.append(directory)
            VALID_DIRECTORIES.add(directory)

    def insert_file(self, name, size):
        if not self.file_exists(name):
            _file = File(name, size)
            self.files.append(_file)
            self.size += _file.size
            self.verify_valid_directory_size(self)
            self.update_parent_directories_size(self.parent, _file.size)

    def update_parent_directories_size(self, parent, size):
        if parent is None:
            return
        parent.size += size
        self.verify_valid_directory_size(parent)
        return self.update_parent_directories_size(parent.parent, size)

    def get_directory_size(self):
        return 0

    def verify_valid_directory_size(self, directory):
        if directory.size > LIMIT_SIZE and directory in VALID_DIRECTORIES:
            VALID_DIRECTORIES.remove(directory)

    def change_directory(self, directory_name):
        for directory in self.directories:
            if directory.name == directory_name:
                return directory

    def change_directory_to_parent(self, args):
        return self.parent


class ReadCommandLines:
    def __init__(self, command_lines):
        self.commands = command_lines

    def parse_command_line(self, line):
        if line.startswith("$ cd"):
            path = line.split(" ")[-1]
            if path == "..":
                return "change_directory_to_parent", [None]
            else:
                return "change_directory", [path]
        elif line == "$ ls":
            return None, [None]
        elif line.startswith("dir"):
            args = line.split(" ")[-1]
            return "insert_directory", [args]
        else:
            size, file_name = line.split(" ")
            return "insert_file", [file_name, int(size)]

    def read_command_lines(self):
        command_lines = []
        for command in self.commands[1:]:
            command_lines.append(self.parse_command_line(command))
        return command_lines


class ExecuteCommandLines:
    def __init__(self, command_lines, directory):
        self.command_lines = command_lines
        self.directory = directory

    def execute_command_lines(self, command_lines, directory):

        if len(command_lines) == 0:
            return 0

        command, args = command_lines[0]
        if command:
            fnc = getattr(directory, command, None)
            changed_directory = fnc(*args)

            if changed_directory:
                print(changed_directory)
                directory = changed_directory
        return self.execute_command_lines(command_lines[1:], directory)

    def execute(self):
        self.execute_command_lines(self.command_lines, self.directory)


def solution(commands):
    file_system = Directory("/")
    VALID_DIRECTORIES.add(file_system)
    rcl = ReadCommandLines(commands)
    command_lines = rcl.read_command_lines()
    ecl = ExecuteCommandLines(command_lines[1:], file_system)
    ecl.execute()
    return file_system



def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    command_lines = ReadFile(dir_path + "/input.txt").get_data_from_line()
    file_system = solution(command_lines)
    print(f"Valid Directories: {VALID_DIRECTORIES}")
    total_size_valid_directories = sum([directory.size for directory in  VALID_DIRECTORIES])
    print(f"Total size Valid Directories {total_size_valid_directories}")
    return file_system
