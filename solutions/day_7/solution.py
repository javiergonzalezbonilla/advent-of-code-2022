import os
from solutions.utils import ReadFile

VALID_DIRECTORIES = set()
LIMIT_SIZE = 100000
TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File: {self.name} -- size: {self.size}"


class Directory:
    def __init__(self, name, parent=None):
        self.directories = []
        self.files = []
        self.parent = parent
        self.name = name
        self.size = 0

    def __repr__(self) -> str:
        return f"Directory Name: {self.name} - size: {self.size}"

    def directory_exists(self, directory_name):
        directory_names = [directory.name for directory in self.directories]
        return directory_name in directory_names

    def file_exists(self, file_name):
        files_names = [_file.name for _file in self.files]
        return file_name in files_names

    def get_size(self):
        def calculate_size(directory, total_size=0):
            total_size += sum([_file.size for _file in directory.files])
            for directory in directory.directories:
                total_size += calculate_size(directory, 0)
            return total_size

        return calculate_size(self, 0)

    def insert_directory(self, directory_name):
        # if not self.directory_exists(directory_name):
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

    def verify_valid_directory_size(self, directory):
        if directory.size > LIMIT_SIZE and directory in VALID_DIRECTORIES:
            VALID_DIRECTORIES.remove(directory)

    def change_directory(self, directory_name):
        for directory in self.directories:
            if directory.name == directory_name:
                return directory

    def change_directory_to_parent(self, args):
        if self.parent is None:
            return self
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
                directory = changed_directory
        return self.execute_command_lines(command_lines[1:], directory)

    def execute(self):
        self.execute_command_lines(self.command_lines, self.directory)


def create_file_system(commands):
    file_system = Directory("/")
    VALID_DIRECTORIES.add(file_system)
    rcl = ReadCommandLines(commands)
    command_lines = rcl.read_command_lines()
    ecl = ExecuteCommandLines(command_lines[1:], file_system)
    ecl.execute()
    return file_system


def find_smallest_directory(file_system):
    def find_directories(directory):
        directories = []
        directories.extend(directory.directories)
        for directory in directory.directories:
            directories.extend(find_directories(directory))
        return directories

    all_directories = find_directories(file_system)
    all_directories.append(file_system)
    all_directories = sorted(all_directories, key=lambda x: x.size, reverse=False)

    available_space = TOTAL_SPACE - file_system.size
    required_space_to_delete = NEEDED_SPACE - available_space
    directory_to_delete = all_directories[0]
    for index, directory in enumerate(all_directories):
        if directory.size <= required_space_to_delete:
            directory_to_delete = directory
            current_index = index
    directory_to_delete = all_directories[current_index + 1]
    return directory_to_delete


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    command_lines = ReadFile(dir_path + "/input.txt").get_data_from_line()

    file_system = create_file_system(command_lines)
    total_size_valid_directories = sum(
        [directory.size for directory in VALID_DIRECTORIES]
    )
    print(f"Valid Directories total size: {total_size_valid_directories}")
    directory_to_delete = find_smallest_directory(file_system)
    print(f"Directory to delete {directory_to_delete}")
