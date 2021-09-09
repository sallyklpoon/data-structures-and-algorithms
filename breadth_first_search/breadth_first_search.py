from queue_ds.queue_using_deque import Queue

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
            return