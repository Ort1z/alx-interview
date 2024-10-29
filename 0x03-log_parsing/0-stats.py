#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print statistics about the accumulated metrics.
    Args:
        total_size: The accumulated file size
        status_codes: Dictionary with accumulated status code counts
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    Parse a log line and extract file size and status code.
    Args:
        line: String containing the log line
    Returns:
        tuple: (file_size, status_code) or None if line is invalid
    """
    try:
        parts = line.split()
        if len(parts) < 7:
            return None
        
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        
        if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
            return None
            
        return (file_size, status_code)
    except (ValueError, IndexError):
        return None


def main():
    """
    Main function to process the log input.
    """
    total_size = 0
    line_count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            result = parse_line(line)
            if result:
                file_size, status_code = result
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()