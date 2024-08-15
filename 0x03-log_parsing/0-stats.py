#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys


def print_stats(sts, size):
    """Prints the cumulative statistics"""
    print("File size: {:d}".format(size))
    for key in sorted(sts.keys()):
        if sts[key] > 0:
            print("{}: {:d}".format(key, sts[key]))

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        """Extract status code and file size"""
        status = parts[-2]
        try:
            size = int(parts[-1])
            total_size += size
        except ValueError:
            continue

        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats(status_codes, total_size)

    print_stats(status_codes, total_size)

except KeyboardInterrupt:
    print_stats(status_codes, total_size)
    raise
