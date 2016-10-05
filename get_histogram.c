#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <sys/timeb.h>
#include <strings.h>

/**
 * file_ptr : the file pointer, ready to be read from.
 * hist: an array to hold 26 long integers.  hist[0] is the
 *       number of 'A', and hist[1] is the number of 'B', etc.
 * block_size: the buffer size to be used.
 * milliseconds: time it took to complete the file scan
 * total_bytes_read: the amount data in bytes read
 *
 * returns: -1 if there is an error.
 */
int get_histogram(
    FILE *file_ptr, 
    long hist[], 
    int block_size, 
    long *milliseconds, 
    long *total_bytes_read
){
    char buffer[block_size];

    // start timer
    struct timeb t;
    ftime(&t);
    unsigned long start_ms = t.time * 1000 + t.millitm;

    for (int i = 0; !feof(file_ptr); i += block_size) {
        // bzero(buffer, block_size);
        fread(buffer, sizeof(char), block_size, file_ptr);
        for (int i = 0; i < block_size; i += 1) {
            // ~~ASCII~~ powers
            hist[(int)buffer[i] - 'A'] += 1;
        }
        *total_bytes_read += (long)block_size;
    }

    // stop timer
    ftime(&t);
    unsigned long stop_ms = t.time * 1000 + t.millitm;

    *milliseconds = stop_ms - start_ms;

    fclose(file_ptr);

    return 0;
}

long hist[26];
long milliseconds;
long filelen;

/**
* Compute the histogram using 2K buffers
*/
int main(int argc, const char * argv[]) {
    if (argc < 2) {
        printf("Usage: get_histogram <filename> <block_size>");
        return 1;
    }

    const char *filename = argv[1];
    FILE *fp;
    fp = fopen(filename, "r");

    int block_size = atoi(argv[2]);

    int ret = get_histogram(fp, 
                            hist, 
                            block_size,
                            &milliseconds,
                            &filelen);

    assert(! (ret < 0));

    // print histogram
    for(int i=0; i < 26; i++) {
        printf("%c : %lu\n", 'A' + i, (long)hist[i]);
    }

    printf("BLOCK SIZE: %d\n", block_size);
    printf("TOTAL BYTES: %lu\n", filelen);
    printf("TIME: %lu milliseconds\n", milliseconds);

}
