# -*- coding: utf-8 -*-
import yaml
from yaml.loader import SafeLoader


class ReadFile:
    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as f:
            self.lines = f.readlines()

    def get_data_separated_by_breakline(self):
        items = []
        all_items = []
        for line in self.lines:
            if line == "\n":
                all_items.append(items)
                items = []
            else:
                items.append(int(line.replace("\n", "")))
        return all_items

    def get_data_from_raw_table(self):
        items = []
        for line in self.lines:
            items.append(line.replace("\n", "").split(" "))
        return items

    def get_data_from_line(self):
        items = []
        for line in self.lines:
            items.append(line.replace("\n", ""))
        return items


def open_yaml(path):
    with open(path, "r") as f:
        data = yaml.load(f, Loader=SafeLoader)
        print(data)
        return data
