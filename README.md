# csc443-a1
[![CircleCI](https://circleci.com/gh/elliottsj/csc443-a1.svg?style=svg&circle-token=67986114ef4010271a2856aee852bffb39468acf)](https://circleci.com/gh/elliottsj/csc443-a1)

[Assignment 1](http://www.cdf.toronto.edu/~csc443h/fall/posted_assignments/a1/a1.html)

### Setup
Using Python 3.5.1:
```shell
pyvenv venv                      # create virtualenv
source venv/bin/activate.fish    # activate virtualenv
pip install -r requirements.txt  # install dependencies
jupyter notebook                 # start jupyter
```

### Contents

* `create_random_file.c`: source for the `create_random_file` program
* `get_histogram.c`: source for the `get_histogram` program
* `CSC443 Assignment 1.ipynb`: source for the report
* `CSC443 Assignment 1.pdf`: PDF render of the report
* `Makefile`: make tasks to build binaries
* `requirements.txt`: pip dependencies to edit the ipynb notebook
* `results_dfs_read.csv`: results for reading files from DFS
* `results_dfs_write.csv`: results for writing files to DFS
* `results_hdd_read.csv`: results for reading files from HDD
* `results_hdd_write.csv`: results for reading files to HDD
* `results_ssd_read.csv`: results for reading files from SSD
* `results_ssd_write.csv`: results for reading files to SSD
* `results_usb_read.csv`: results for reading files from USB
* `results_usb_write.csv`: results for reading files to USB
