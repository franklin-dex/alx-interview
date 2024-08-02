#!/usr/bin/python3
"""Solves the lock boxes puzzle using Union-Find"""

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened using Union-Find.

    Parameters:
    boxes: A list where each element is a list of keys contained in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    uf = UnionFind(n)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
                uf.union(box_index, key)

    return len(set(uf.find(i) for i in range(n))) == 1

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
