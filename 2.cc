#include <iostream>

int main()
{
    int sum = 0;
    int max = 4000000;

    int j = 0;
    int k = 1;

    for( int fib = 0; fib < max; fib = k + j ) {
        if( 0 == fib%2) {
            sum += fib;
        }

        j = k;
        k = fib;
    }

    std::cout << "The sum of the integers is: " << sum
              << std::endl;

    return 0;
}
