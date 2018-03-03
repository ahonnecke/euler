#include <iostream>
#include <deque>

// 2520 is the smallest number that can be divided by each of the numbers
// from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of
// the numbers from 1 to 20?

int main()
{
    int max = 100;
    int sum = 0;
    long sumofSquares = 0;
    long squareOfSums = 0;

    for( int i=0 ; i <= max; i++ ) {
        sumofSquares += i*i;
        sum += i;
    }
    std::cout
        << " the sum of the squares of the first "
        << max
        << " natural numbers is "
        << sumofSquares
        << std::endl
        << " the square of the sum of the first "
        << max
        << " natural numbers is "
        << sum * sum
        << std::endl
        << " the difference is "
        << (sum * sum) - sumofSquares
        << std::endl;


    return 0;
}
