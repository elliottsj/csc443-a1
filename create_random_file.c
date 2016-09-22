#include <stdio.h>
#include <stdlib.h>

/**
 * populate a random array (which is already
 * allocated with enough memory to hold n bytes.
 */
char* random_array(char *array, long bytes) {
    for (int i = 0; i < bytes; i++) {
        char random_char = 'A' + (rand() % 26);
        array[i] = random_char;
    }
    return array;
};

int main(int argc, const char * argv[]) {
    FILE *fp;
    const char *file_name = argv[1];
    int total_size = atoi(argv[2]);
    int block_size = atoi(argv[3]);
    if (file_name == NULL) {
        return 0;
    }
    // allocate a fixed amount of memory
    char buffer[block_size];
    // calculate remainder as block_size/total_size isnt clean
    int remainder = total_size % block_size;
    for(int i = 0;i < total_size; i += block_size) {
        const char *temp_buffer = random_array(buffer, block_size);
        fp = fopen(file_name, "w+");
        fwrite(temp_buffer, block_size, 1, fp);
        fclose(fp);
    }
    return 0;
}