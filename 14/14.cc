#include <iostream>
#include <stack>
#include <math.h>

//Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

int main()
{
    std::stack<long> collatz;
    int max = 0;
    int maxSize = 0;
    int size = 0;
    long n = 0;

    for(long i = 12; i <= 1000000; i++) {
        collatz.empty();

        // std::cout
        //     << i;
        n=i;
        size=1;
        while(n > 1) {
            collatz.push(n);
            // std::cout
            //     << " -> "
            //     << n;

            if (0 == n % 2) {
                n = n/2;
            } else {
                n = (3*n)+1;
            }
            size++;
        }
        // std::cout
        //     << " -> 1"
        //     << std::endl;

//        size = collatz.size();
        if (maxSize < size) {
            max = i;
            maxSize = size;
        }
    }
    std::cout
        << std::endl;

    // while(!collatzMax.empty()) {
    //     int top = collatzMax.top();
        std::cout
            << "starting number: "
            << max
            << " (length: "
            << maxSize
            << ")";

    //     collatzMax.pop();
    // }

    std::cout  << std::endl;

    return 0;
}
