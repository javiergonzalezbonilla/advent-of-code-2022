import os
from functools import reduce

from solutions.utils import ReadFile


def manhattan_distance(point1, point2):
    return sum(abs(val1 - val2) for val1, val2 in zip(point1, point2))


max_scenic_score = 0


def get_visible_trees(grid):
    field_height = len(grid)
    field_width = len(grid[0])

    def is_tree_visible(position_x, position_y, tree_height):
        tree_positions = [
            {
                "direction": [-1, 0],
                "limit": 0,
                "enabled": True,
                "distance": 1,
                "visible": False,
                "name": "LEFT",
            },
            {
                "direction": [0, -1],
                "limit": 0,
                "enabled": True,
                "distance": 1,
                "visible": False,
                "name": "DOWN",
            },
            {
                "direction": [1, 0],
                "limit": field_height - 1,
                "enabled": True,
                "distance": 1,
                "visible": False,
                "name": "UP",
            },
            {
                "direction": [0, 1],
                "limit": field_width - 1,
                "enabled": True,
                "distance": 1,
                "visible": False,
                "name": "RIGHT",
            },
        ]

        multiplier = 1
        while [
            position["enabled"] for position in tree_positions if position["enabled"]
        ]:

            tree_positions = analyze_tree_positions(
                position_x, position_y, tree_height, tree_positions, multiplier,
            )

            multiplier += 1

        scenic_score = reduce(
            lambda x, y: x * y, [position["distance"] for position in tree_positions]
        )

        visible = any([position["visible"] for position in tree_positions])
        return visible, scenic_score

    def analyze_tree_positions(
        position_x, position_y, tree_height, tree_positions, multiplier,
    ):
        for tree_position in tree_positions:
            if tree_position["enabled"]:
                offset_y, offset_x = tree_position["direction"]
                offset_y *= multiplier
                offset_x *= multiplier

                current_distance = get_absolute_1d_distance(
                    position_x, position_y, offset_y, offset_x
                )

                visited_tree_y = position_y + offset_y
                visited_tree_x = position_x + offset_x

                visited_tree_height = int(grid[visited_tree_y][visited_tree_x])

                if tree_height <= visited_tree_height:
                    tree_position["enabled"] = False
                    tree_position["distance"] = multiplier

                if current_distance == tree_position["limit"]:
                    if tree_height > visited_tree_height:
                        tree_position["visible"] = True
                    tree_position["enabled"] = False
                    tree_position["distance"] = multiplier

        return tree_positions

    def get_absolute_1d_distance(position_x, position_y, offset_y, offset_x):
        limit = [
            pos + offset
            for pos, offset in [[position_x, offset_x], [position_y, offset_y]]
            if offset != 0
        ][0]

        return limit

    max_scenic_score = 0

    visible_trees = 0
    for y_pos in range(1, field_height - 1):
        for x_pos in range(1, field_width - 1):
            current_tree_height = int(grid[y_pos][x_pos])
            visible, scenic_score = is_tree_visible(x_pos, y_pos, current_tree_height)

            if visible:
                visible_trees += 1
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    all_visible_trees = visible_trees + 2 * (field_width + field_height) - 4

    print(f"\n Total trees {field_height * field_width}")
    print(f"Total visible trees {all_visible_trees}")
    print(f"Max scenic score {max_scenic_score}")


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    grid = ReadFile(dir_path + "/input.txt").get_data_from_line()
    get_visible_trees(grid)


# sample - visible trees 21
# sample - scenic score 8

# visible_trees 1715
# Max scenic score 374400
