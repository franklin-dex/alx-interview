#!/usr/bin/python3
"""Solves the lock boxes puzzle using an iterative DFS approach"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes: A list where each element is a list of keys contained in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
