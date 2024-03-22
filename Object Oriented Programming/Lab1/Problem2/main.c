#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

// Alice forgot her card�s PIN code.She remembers that her PIN code had 4 digits, all the digits were distinct in decreasing order, and that the sum of these digits was 24.
// This C program that prints, on different lines, all the PIN codes which fulfill these constraints. 

int main(int argc, char* argv[]) {


    for (int i = 9; i >= 0; i--)
        for (int j = i - 1; j >= 0; j--)
            for (int k = j - 1; k >= 0; k--)
                if (24 - (i + j + k) >= 0 && 24 - (i + j + k) < 10 && 24 - (i + j + k) < k)
                    printf("%d%d%d%d\n", i, j, k, 24 - (i + j + k));

    return 0;
}

