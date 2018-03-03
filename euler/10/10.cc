#include <iostream>

// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

bool isPrime(long possiblePrime) {
    long max = possiblePrime / 2;

    if(possiblePrime < 2)
    {
        return false;
    }

    if(possiblePrime < 3)
    {
        return true;
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
    long max = 2000000;
    double sum = 0;

    for(long i = 0; i <= max ; i++)
    {
        if(isPrime(i)) {
            // std::cout
            //     << i
            //     << " is prime "
            //     << std::endl;
            sum = sum+i;
        }
    }


    std::cout
        << " the sum of the primes less than "
        << max
        << " is "
        << std::fixed
        << sum
        << std::endl;

    return 0;
}
