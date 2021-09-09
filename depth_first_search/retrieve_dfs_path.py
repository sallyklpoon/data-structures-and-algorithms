"""
A helper function to retrieve the path of a depth first search
"""


def get_path(search_record: dict, start: str, goal: str) -> list:
    """Given a dictionary containing a DFS search path, return the path from start to goal of the DFS.

    Code adapted from Robin Andrews

    :param search_record: a Dictionary
    :param start: a String
    :param goal: a String
    :precondition: start and goal are strings within a map, the passed search record is a valid
                   DFS predecessor dictionary
    :postcondition: return a list of the path for a DFS from start to finish at a goal.
    :return:
    """
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = search_record[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == '__main__':
    my_search_path = {"A": None,  "B": "A", "D": "A", "E": "D", "G": "D", "H": "G", "I": "H"}
    print(get_path(my_search_path, "A", "I"))