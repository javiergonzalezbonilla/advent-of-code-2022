# -*- coding: utf-8 -*-

class ReadFile:
    def __init__(self,path):
        self.path = path
        with open(self.path, 'r') as f:
            self.lines = f.readlines()

    def data_separated_by_breakline(self):
        items = []
        all_items = []
        for line in  self.lines:
            if line == "\n":
                all_items.append(items)
                items = [] 
            else:
                items.append(int(line.replace("\n", "")))
        return all_items