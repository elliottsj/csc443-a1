#!/usr/bin/env python3

import csv
import os
import shutil
import subprocess
import sys


def get_histogram(filename, block_size):
    """
    Execute ./get_histogram with the given arguments and return the number of milliseconds
    it took to create the file.
    """
    result = subprocess.run(
        ['./get_histogram', filename, str(block_size)],
        stdout=subprocess.PIPE,
    )
    # parse the result to get the desired time
    return int(result.stdout.split()[-2])


def main():
    """
    Call ./get_histogram to read mybigfile.txt using ten different block sizes,
    each in a range of 100B to 3MB.
    """
    block_sizes = [
        128,           # 128 B
        1 * 2 ** 10,   # 1 KiB
        4 * 2 ** 10,   # 4 KiB
        8 * 2 ** 10,   # 8 KiB
        64 * 2 ** 10,  # 64 KiB
        128 * 2 ** 10,  # 128 KiB
        512 * 2 ** 10,  # 512 KiB
        1 * 2 ** 20,   # 1 MiB
        2 * 2 ** 20,   # 2 MiB
        3 * 2 ** 20,   # 3 MiB
    ]
    total_size = 100 * 2 ** 20  # 100 MiB

    if os.path.exists('./out'):
        shutil.rmtree('./out')
    os.mkdir('./out')
    csvwriter = csv.DictWriter(
        sys.stdout,
        fieldnames=('block_size', 'milliseconds_elapsed', 'total_size'),
        dialect='unix'
    )
    csvwriter.writeheader()
    for block_size in block_sizes:
        for i in range(50):
            filename = './mybigfile.txt'
            ms_elapsed = get_histogram(
                filename,
                block_size,
            )
            csvwriter.writerow({
                'block_size': block_size,
                'milliseconds_elapsed': ms_elapsed,
                'total_size': total_size,
            })

if __name__ == '__main__':
    main()
