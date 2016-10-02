#!/usr/bin/env bash
# Unofficial bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

# Show commands before executing
set -o xtrace

make
./experiment_create_random_file.py
