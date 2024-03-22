#include <stdio.h>
#include <limits.h>
#include "tests.h"

// Using the function that you wrote for problem 2, write a function that computesand returns an array with all the positions of the occurrences of a character in a string.
const char* my_strchr(const char* s, char character){
    while (*s) {
        if (*s == character) {
            return s;
        }
        s++;
    }
    if (*s == character) {
        return s;
    }
    return NULL;
}

void find_all( const char * str, char character, int*  positions, unsigned int cap, unsigned int * l){
    const char *found = NULL;
    unsigned int i = 0;
    *l = 0;
    while ((found = my_strchr(str, character)) != NULL && i < cap) {
        positions[i++] = found - str;
        str = found + 1;
        (*l)++;
    }
}

int main()
{
#if  ENABLE_TESTS > 0
    run_tests(true);
#endif 

    return 0;
}
