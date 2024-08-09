#!/usr/bin/python3

"""
This module contains the minOperations function.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters in the file.

    Parameters:
    n (int): The number of characters desired.

    Returns:
    int: The minimum number of operations required, or 0 if n cannot be achieved.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations