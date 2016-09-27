#include <stdio.h>
#include <stdlib.h>
#include <sys/timeb.h>

/**
 * populate a random array (which is already
 * allocated with enough memory to hold n bytes.
 */
void random_array(char *array, long bytes) {
    for (int i = 0; i < bytes; i++) {
        char random_char = 'A' + (rand() % 26);
        array[i] = random_char;
    }
};

int main(int argc, const char * argv[]) {
    if (argc < 4) {
        printf("Usage: create_random_file <filename> <total_size> <block_size>");
        return 1;
    }
    FILE *fp;
    const char *file_name = argv[1];
    int total_size = atoi(argv[2]);
    int block_size = atoi(argv[3]);
    // allocate a fixed amount of memory
    char buffer[block_size];
    // calculate remainder as block_size/total_size may not be clean
    int remaining_bytes = total_size % block_size;

    // start timer
    struct timeb t;
    ftime(&t);

    fp = fopen(file_name, "w+");
    for (int i = 0; i < total_size; i += block_size) {
        random_array(buffer, block_size);
        fwrite(buffer, block_size, 1, fp);
    }

    // write remainder
    random_array(buffer, remaining_bytes);
    fwrite(buffer, remaining_bytes, 1, fp);
    fflush(fp);

    // stop timer
    unsigned long long now_in_ms = t.time * 1000 + t.millitm;

    fclose(fp);
    printf("%llu", now_in_ms);
    printf("\n");
    return 0;
}
