#!/usr/bin/env bash
# Unofficial bash strict mode: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

make
./experiment_create_random_file.py
