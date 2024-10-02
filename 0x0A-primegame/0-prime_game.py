#!/usr/bin/python3
"""
Prime Game - Determines the winner between Maria and
Ben after x rounds.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
    x: The number of rounds.
    nums: A list of integers where each integer represents
    the range of numbers in each round.

    Returns:
    str: The name of the player that won the most rounds
    (Maria or Ben).
    If the winner cannot be determined, return None.
    """
    if x <= 0 or not nums:
        return None

    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes = [i for i in range(2, n + 1) if sieve[i]]
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    prime_counts = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
