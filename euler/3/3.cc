#include <iostream>

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

bool isPrime(long possiblePrime) {
    long max = possiblePrime; // 3;

    if( 1 == possiblePrime || 2 == possiblePrime)
    {
        return true;
    }

    for( long i = 2; i < max; i++ ) {
        if( 0 == possiblePrime % i ) {
            // std::cout << possiblePrime
            //           << " is divisible by "
            //           << i
            //           << std::endl;

            return false;
        }
    }

    return true;
}

int main()
{
    long max = 600851475143;
    //long max = 10000000000;
    //long halfmax = max/2;
    //max = 90000;

    //int max = 100;

    // if(isPrime(max)) {
    //     std::cout << max
    //               << " is prime "
    //               << std::endl;
    // }

    for( long i = 1; i < max/2; i++ ) {
        if( 0 == i % 100000000 ) {
            std::cout << i / 100000000
                      << std::endl;
        }

        if( 0 == max % i ) {
            std::cout << i
                      << " is a factor"
                      << " of "
                      << max;
            if(isPrime(i)) {
                std::cout << " and is prime too"
                          << std::endl;
            }
            std::cout << std::endl;
        } else {
            // std::cout << i
            //           << " is not a factor"
            //           << std::endl;
        }
    }

    return 0;
}
