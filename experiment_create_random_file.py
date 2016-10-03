#!/usr/bin/env python3

import csv
import os
import shutil
import subprocess
import sys

def create_random_file(filename, total_size, block_size):
    """
    Execute ./create_random_file with the given arguments and return the number of milliseconds
    it took to create the file.
    """
    result = subprocess.run(
        ['./create_random_file', filename, str(total_size), str(block_size)],
        stdout=subprocess.PIPE,
    )
    return int(result.stdout)


def main():
    """
    Call ./create_random_file to create ten 50 MiB files, each using a unique block size
    ranging from 128 B to 2 MiB
    """
    block_sizes = [
        128,           # 128 B
        512,           # 512 B
        1 * 2 ** 10,   # 1 KiB
        4 * 2 ** 10,   # 4 KiB
        8 * 2 ** 10,   # 8 KiB
        64 * 2 ** 10,  # 64 KiB
        128 * 2 ** 10, # 128 KiB
        512 * 2 ** 10, # 512 KiB
        1 * 2 ** 20,   # 1 MiB
        2 * 2 ** 20,   # 2 MiB
    ]

    # Write files to ./out/file_{block_size}
    if os.path.exists('./out'):
        shutil.rmtree('./out')
    os.mkdir('./out')
    csvwriter = csv.DictWriter(
        sys.stdout,
        fieldnames=('block_size', 'milliseconds_elapsed'),
        dialect='unix'
    )
    csvwriter.writeheader()
    for block_size in block_sizes:
        filename = './out/file_{block_size}.bin'.format(block_size=block_size)
        ms_elapsed = create_random_file(
            filename,
            50 * 2 ** 20,  # 50 MiB
            block_size,
        )
        csvwriter.writerow({'block_size': block_size, 'milliseconds_elapsed': ms_elapsed})

if __name__ == '__main__':
    main()
