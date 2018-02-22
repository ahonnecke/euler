#include <iostream>

// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
//     that the 6th prime is 13.
//     What is the 10 001st prime number?

bool isPrime(long possiblePrime) {
    long max = possiblePrime / 2;

    if( 2 == possiblePrime)
    {
        return true;
    }

    if(possiblePrime < 2)
    {
        return false;
    }

    for( long i = 2; i <= max; i++ ) {
        if( 0 == possiblePrime % i ) {
            return false;
        }
    }

    return true;
}

int main()
{
    long max = 100000000000;
    int j = 0;

    for( int i=1 ; i <= max; i++ )
    {
        if(isPrime(i) )
        {
            j++;

            if(j == 10001 || j == 6 ) {
                std::cout
                    << i
                    << " is the "
                    << j
                    << "th prime."
                    << std::endl;
            }
        }
    }

    return 0;
}
