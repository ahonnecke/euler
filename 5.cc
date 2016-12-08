#include <iostream>
#include <deque>

// 2520 is the smallest number that can be divided by each of the numbers
// from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of
// the numbers from 1 to 20?

long divisible(long i, long j) {
    for( j = 1; j < 20; j++ ) {
        if(0 != i%j) {
            return false;
        }
    }

    return true;
}

long main()
{
    long i = 0;
    long j = 0;

    for( i = 1; i < 2600000000; i++ ) {
        if(divisible(i, j)) {
            //if(j > 8) {
                std::cout
                    << i
                    << " is divisible by "
                    << j
                    << " with no remainder"
                    << std::endl;
                //}
        }
    }

    return 0;
}
