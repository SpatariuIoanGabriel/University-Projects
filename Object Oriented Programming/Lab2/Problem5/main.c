#include <math.h>
#include <stdio.h>
#include <limits.h>
#include <time.h>
#include <stdlib.h>

#include "tests.h"

void generateAllCombinations(int** numbers, char** operators) {
}

int main(int argc, char** argv) {
int mode = FULL_MODE;
if (argc > 1) {
    if (strcmp(argv[1], "-h") == 0) {
        printf("The 24 puzzle is a math game in which the player is given 4 digits and must combine them using +, -, *, and / operators to obtain a result of 24.\n");
        printf("Usage: %s [options]\n", argv[0]);
        printf("Options:\n");
        printf("  -h\tDisplay this help message and exit.\n");
        printf("  -s\tSave all possible solutions to a file and exit.\n");
        printf("  -e\tPlay the game in easy mode.\n");
        printf("If no options are specified, the game is played in full mode.\n");
        return 0;
    } 
    else if (strcmp(argv[1], "-s") == 0) {
        int** numbers = malloc(NUM_COMBINATIONS * sizeof(int*));
        char** operators = malloc(NUM_COMBINATIONS * sizeof(char*));
        generateAllCombinations(numbers, operators);
        FILE* f = fopen("solution.txt", "w");
        for (int i = 0; i < NUM_COMBINATIONS; i++) {
            fprintf(f, "%d %d %d %d %c %c %c\n", numbers[i][0], numbers[i][1], numbers[i][2], numbers[i][3], operators[i][0], operators[i][1], operators[i][2]);
        }
        fclose(f);
        printf("All solutions saved to solution.txt.\n");
        free(numbers);
        free(operators);
        return 0;
    } 
    else if (strcmp(argv[1], "-e") == 0) {
        mode = EASY_MODE;
    } 
    else {
        printf("Unknown option: %s\n", argv[1]);
        return 1;
    }
}

srand(time(NULL));
int digits[NUM_DIGITS];
char operators[NUM_OPERATORS];
int result;
char choice;
int valid = 0;

do {
    if (mode == EASY_MODE) {
        int easy_combinations[7][4] = {{1, 1, 4, 6}, {1, 1, 3, 8}, {1, 2, 2, 6}, {1, 2, 3, 4}, {1, 1, 3, 9}, {4, 4, 4, 6}, {1, 8, 8, 8}};
        int index = rand() % 7;
        for (int i = 0; i < NUM_DIGITS; i++) {
            digits[i] = easy_combinations[index][i];
        }
    } else {
        for (int i = 0; i < NUM_DIGITS; i++) {
            digits[i] = rand() % 10;
        }
    }

    printf("The digits are: %d %d %d %d\n", digits[0], digits[1], digits[2], digits[3]);
#if ENABLE_TESTS > 0
    run_tests(true);
#endif
    return 0;

}
