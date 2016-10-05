all: create_random_file get_histogram

create_random_file: create_random_file.c
	gcc -std=c99 -g -Wall $^ -o $@

get_histogram: get_histogram.c
	gcc -std=c99 -g -Wall $^ -o $@
