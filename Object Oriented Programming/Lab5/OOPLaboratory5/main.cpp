#include "BigInteger.h"
#include "big_int_test.h"

#include <iomanip>
#include <iostream>
using namespace std;


BigInteger computeNthFibonacci(unsigned int n) {
    BigInteger a("0"), b("1"), c("1");
    if (n == 0)
        return c;
    n--;
    while (n != 0) {
        c = a + b;
        b = a;
        a = c;
        n--;
    }
    return b;
}


int main() {
#if ENABLE_TESTS > 0
    run_bigint_tests(true);
#endif

    BigInteger crt("-1");
    BigInteger prev("-1");
    bool isOverflow = false;
    for (int n = 0; n < 200; n+=10) {
        prev = crt;
        crt = computeNthFibonacci(n);
        if (crt < prev)
            isOverflow = true;
        cout << setw(5) << n << "\t" << setw(70)<<crt<<"\t"<<(isOverflow ? string(RED)+string("OVERFLOW !!!! ")+string(NC) : "") << endl;
    }

    return 0;
}
