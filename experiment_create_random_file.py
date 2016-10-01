#!/usr/bin/env python3

import subprocess

def create_random_file(filename, total_size, block_size):
    result = subprocess.run(
        ['./create_random_file', filename, str(total_size), str(block_size)],
        stdout=subprocess.PIPE,
    )
    return int(result.stdout)


def main():
    elapsed_ms = create_random_file('file.bin', 2 ** 26, 2 ** 14)
    print('Created file.bin using {} milliseconds'.format(elapsed_ms))

if __name__ == '__main__':
    main()
