#include <stdio.h>
#include <limits.h>
#include "tests.h"

// Write a function that takes as an input an array of integer numbers (both positive and negative numbers and returns the value of the triplet with the maximum product, as well as the elements that form this triplet (in increasing order). 
// Use pass by pointer/address to return the elements that form that triplet. 
// Think about the appropriate data type for the result. If the size of the array is less than 3, you should return the minimum
// representable value of the data type and the elements that form the triplet should be set to 0.
long long computeMaxTriplet(int arr[], unsigned int sz, int *t1, int *t2, int *t3) {
    if (sz < 3) {
        printf("The array has less than 3 elements. Application will now stop.\n");
        return LLONG_MIN;
    }

    long long max_product = LLONG_MIN;
    *t1 = *t2 = *t3 = 0;

    for (int i = 0; i < sz - 2; i++) {
        for (int j = i + 1; j < sz - 1; j++) {
            for (int k = j + 1; k < sz; k++) {
                long long product = (long long)arr[i] * arr[j] * arr[k];
                if (product > max_product) {
                    max_product = product;
                    *t1 = arr[i];
                    *t2 = arr[j];
                    *t3 = arr[k];
                }
            }
        }
    }

    printf("The maximum triplet is (%d, %d, %d) with a product of %lld.\n", *t1, *t2, *t3, max_product);
    return max_product;
}

int main() {
#if ENABLE_TESTS > 0
    run_tests(true);
#endif
    int arr[100], n, t1, t2, t3;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    long long max_product = computeMaxTriplet(arr, n, &t1, &t2, &t3);
    return 0;
}
