#!usr/bin/python3
"""
Lockboxes
method that determines if all the boxes can be opened
"""

from collections import deque

def canUnlockAll(boxes):
    """
    determines if all boxes can be opened
    Args:
    boxes: A list where each element is a list of keys
    contained in that box
    returns:
    bool: True if all boxes can be opened and false if otherwise
    """

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))