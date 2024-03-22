#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "tests.h"

// Substitution cipher or Caesar�s cipher.

// This program which reads a natural number n and a string s. The string s is encoded using Caesar�s cipher with a displacement of n (either positive or negative).
// The program decodes the message and display it on the screen. Punctuation marks and numbers are left as they are.


// DO NOT CHANGE THE SIGNATURE OF THIS METHOD
void encrypt(char s[], int n){
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (isalpha(s[i]))
        {
            if (isupper(s[i]))
            {
                s[i] = (s[i] - 'A' + n) % 26 + 'A';
            }
            else
            {
                s[i] = (s[i] - 'a' + n) % 26 + 'a';
            }
        }
    }
}

int main(){
    // To enable the tests, ctrl+click on ENABLE_TESTS (or go to the file "tests.h") and change the line
    // #define ENABLE_TESTS 0
    // to:
    // #define ENABLE_TESTS 1
#if ENABLE_TESTS > 0
    run_tests(true);
#endif

    int n;
    char s[1000];
    scanf("%d", &n);
    getchar();
    fgets(s, 1000, stdin);
    encrypt(s, n);
    printf("%s", s);

    return 0;
}