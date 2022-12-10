import os
import pdb
from solutions.utils import ReadFile


def get_visible_trees(grid):
    field_height = len(grid)
    field_width = len(grid[0])

    def is_tree_visible(position_x, position_y, tree_height):

        base_positions = [
            {"base_pos": [-1, 0], "limit": 0, "enabled": True},
            {"base_pos": [0, -1], "limit": 0, "enabled": True},
            {"base_pos": [1, 0], "limit": field_height - 1, "enabled": True},
            {"base_pos": [0, 1], "limit": field_width - 1, "enabled": True},
        ]

        visible = False

        multiplier = 1
        while (not visible) and base_positions:

            base_positions, visible = visible_at_a_given_distance(
                position_x, position_y, tree_height, base_positions, multiplier,
            )

            base_positions = [
                position for position in base_positions if position["enabled"]
            ]

            multiplier += 1
        return visible

    def visible_at_a_given_distance(
        position_x,
        position_y,
        tree_height,
        relative_tree_positions_to_check,
        multiplier,
    ):
        visible_on_directions = [False, False, False, False]
        for index, position in enumerate(relative_tree_positions_to_check):

            offset_y, offset_x = position["base_pos"]
            offset_y *= multiplier
            offset_x *= multiplier

            current_distance = get_current_distance(
                position_x, position_y, offset_y, offset_x
            )

            visited_tree_y = position_y + offset_y
            visited_tree_x = position_x + offset_x

            visited_tree_height = int(grid[visited_tree_y][visited_tree_x])

            if tree_height <= visited_tree_height:
                position["enabled"] = False

            if current_distance == position["limit"]:
                if tree_height > visited_tree_height:
                    visible_on_directions[index] = True
                position["enabled"] = False

        return relative_tree_positions_to_check, any(visible_on_directions)

    def get_current_distance(position_x, position_y, offset_y, offset_x):
        limit = [
            pos + offset
            for pos, offset in [[position_x, offset_x], [position_y, offset_y]]
            if offset != 0
        ][0]

        return limit

    visible_trees = 0
    for y_pos in range(1, field_height - 1):
        for x_pos in range(1, field_width - 1):
            current_tree_height = int(grid[y_pos][x_pos])
            if is_tree_visible(x_pos, y_pos, current_tree_height):
                visible_trees += 1

    print(f"\n Total trees {field_height * field_width}")

    all_visible_trees = visible_trees + 2 * (field_width + field_height) - 4
    print(f"Total visible trees {all_visible_trees}")


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    grid = ReadFile(dir_path + "/input.txt").get_data_from_line()
    get_visible_trees(grid)


# sample - 21
# current reponse 1715
