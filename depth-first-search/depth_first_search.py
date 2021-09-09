from retrieve_dfs_path import get_path
from stacks.stack import Stack


def OFFSETS() -> dict:
    return {
        "right": (0, 1),
        "left": (0, -1),
        "down": (1, 0),
        "up": (-1, 0)
    }


def dfs(maze, start, goal):

    stack = Stack()
    stack.add(start)  # Add start to our stack
    predecessors = {start: None}

    while stack:    # Stack not empty
        current_location = stack.pop()
        if current_location == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, column_offset = OFFSETS()[direction]
            neighbour = (current_location[0] + row_offset, current_location[1] + row_offset)
            if neighbour in maze and neighbour not in predecessors:
                stack.add(neighbour)
                predecessors[neighbour] = current_location
    return None
