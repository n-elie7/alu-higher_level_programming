#!/usr/bin/python3
import sys
"""101-stats.py"""

# Valid status codes
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0

def print_stats():
    """Prints the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(codes.keys(), key=int):
        if codes[code] > 0:
            print("{}: {}".format(code, codes[code]))

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.strip().split()

        # Extract file size (last element)
        try:
            total_size += int(parts[-1])
        except Exception:
            pass

        # Extract status code (2nd last element)
        if len(parts) > 1:
            status = parts[-2]
            if status in codes:
                codes[status] += 1

        # Print every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final print after processing all input
print_stats()
