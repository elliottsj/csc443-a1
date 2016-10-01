create_random_file: create_random_file.c
	gcc -std=c99 -g -Wall $^ -o $@
