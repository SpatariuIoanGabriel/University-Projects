#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include "complex_test.h"
#include <iostream>


int main(int argc, char** argv) {

#if ENABLE_TESTS > 0
    run_complex_tests(true);
#endif
    // TODO your code here
    Complex c;
    /*std::cin >> c;*/

    return 0;
}