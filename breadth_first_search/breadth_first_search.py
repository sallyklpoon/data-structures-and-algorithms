from queue_ds.queue_using_deque import Queue
from depth_first_search.retrieve_dfs_path import get_path


def OFFSETS() -> dict:
    return {
        "right": (0, 1),
        "left": (0, -1),
        "down": (1, 0),
        "up": (-1, 0)
    }


def bfs(maze: list, start: tuple, goal: tuple):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while queue:
        current = queue.dequeue()
        if current == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, column_offset = OFFSETS()[direction]
            neighbour = (current[0] + row_offset, current[1] + column_offset)
            if neighbour in maze and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current

