#include <iostream>
#include <stack>

//What is the value of the first triangle number to have over five hundred divisors?

int countDivisors(long input) {
    int divisors = 0;

    // std::cout
    //     << input
    //     << " is divisible by ";

    for( int i = 1; i <= input-1; i++ ) {
        if( 0 == input % i ) {
            divisors++;
            // std::cout
            //     << ", "
            //     << i;
        }
    }
    // std::cout
    //     << std::endl;

    return divisors;
}

int main()
{
    int divisors = 0;
    int tri = 1;
    int i=1;

    while(i++) {
        divisors = countDivisors(tri);

        if(divisors > 4) {
            std::cout
                // << std::endl
                << tri
                << " has "
                << divisors
                << " divisors "
                << std::endl;

            return 0;
        }
        tri = tri + i;
    }

    return 0;
}
