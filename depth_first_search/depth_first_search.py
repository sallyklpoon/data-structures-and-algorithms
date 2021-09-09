from retrieve_dfs_path import get_path
from stacks.stack import Stack


def OFFSETS() -> dict:
    return {
        "right": (0, 1),
        "left": (0, -1),
        "down": (1, 0),
        "up": (-1, 0)
    }


def dfs(maze: list, start: tuple, goal: tuple) -> (list or None):
    """Return the first DFS solution to a maze given a start and end goal.

    Code adapted from Robin Andrews.

    :param maze: A list of coordinates within a maze
    :param start: A tuple of coordinates
    :param goal: A tuple of coordinates
    :return: a list of the coordinates from start to goal of the path
    """
    stack = Stack()
    stack.add(start)  # Add start to our stack
    predecessors = {start: None}    # Current position cannot have predecessor

    while stack:    # Stack not empty
        current_location = stack.pop()
        if current_location == goal:
            return get_path(predecessors, start, goal)  # Done because we are at goal
        for direction in ["up", "right", "down", "left"]:
            row_offset, column_offset = OFFSETS()[direction]
            neighbour = (current_location[0] + row_offset, current_location[1] + row_offset)
            if neighbour in maze and neighbour not in predecessors:
                stack.add(neighbour)
                predecessors[neighbour] = current_location
    return None
