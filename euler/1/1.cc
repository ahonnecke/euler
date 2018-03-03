#include <iostream>

int main()
{
    int sum = 0;

    for( int i = 0; i < 1000; i = i + 1 ) {
        if(0 == i%3 || 0 == i%5) {
            sum += i;
        }
    }

    std::cout << std::endl
              << "The sum of the integers is: " << sum
              << std::endl;                    // output results

    return 0;
}
