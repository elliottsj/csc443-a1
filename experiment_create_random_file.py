#!/usr/bin/env python3

import csv
import glob
import os
import shutil
import subprocess
import sys


def create_random_file(filename, total_size, block_size):
    """
    Return the number of milliseconds it took to create the file.

    Execute ./create_random_file with the given arguments.
    """
    result = subprocess.run(
        [
            os.path.join(os.path.dirname(os.path.realpath(__file__)), './create_random_file'),
            filename,
            str(total_size),
            str(block_size),
        ],
        stdout=subprocess.PIPE,
    )
    return int(result.stdout)


def main():
    """
    Call ./create_random_file to create ten 50 MiB files, each using a unique block size
    ranging from 128 B to 2 MiB
    """
    # Write files to ./<output_directory>/file_{block_size}
    if len(sys.argv) < 2:
        print('Usage: experiment_create_random_file <output_directory>')
        sys.exit(1)
    output_directory = sys.argv[1]
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    for f in glob.glob(os.path.join(output_directory, '*')):
        os.remove(f)

    block_sizes = [
        128,           # 128 B
        512,           # 512 B
        1 * 2 ** 10,   # 1 KiB
        4 * 2 ** 10,   # 4 KiB
        8 * 2 ** 10,   # 8 KiB
        64 * 2 ** 10,  # 64 KiB
        128 * 2 ** 10,  # 128 KiB
        512 * 2 ** 10,  # 512 KiB
        1 * 2 ** 20,   # 1 MiB
        2 * 2 ** 20,   # 2 MiB
    ]
    total_size = 100 * 2 ** 20  # 50 MiB

    csvwriter = csv.DictWriter(
        sys.stdout,
        fieldnames=('block_size', 'milliseconds_elapsed', 'total_size'),
        dialect='unix'
    )
    csvwriter.writeheader()
    for block_size in block_sizes:
        # Create and delete 50 files using the given block size
        for i in range(50):
            filename = os.path.join(
                output_directory,
                './file_{block_size}_{index}.bin'.format(block_size=block_size, index=i)
            )
            ms_elapsed = create_random_file(
                filename,
                total_size,
                block_size,
            )
            csvwriter.writerow({
                'block_size': block_size,
                'milliseconds_elapsed': ms_elapsed,
                'total_size': total_size,
            })
            os.remove(filename)

if __name__ == '__main__':
    main()
