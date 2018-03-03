#include <iostream>
#include <deque>

// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.
bool isPalindrome(std::deque<int> &possiblePalindrome) {
    // for (std::deque<int>::iterator it = possiblePalindrome.begin(); it != possiblePalindrome.end(); ++it) {
    //     std::cout << ' ' << *it;
    // }

    // std::cout << '\n';

    if(1 == possiblePalindrome.size()) {
        return true;
    }

    if(2 == possiblePalindrome.size()) {
        return (possiblePalindrome.front() == possiblePalindrome.back());
    }

    if(possiblePalindrome.front() == possiblePalindrome.back()) {
        possiblePalindrome.pop_front();
        possiblePalindrome.pop_back();

        return isPalindrome(possiblePalindrome);
    }

    return 0;
}

bool isPalindrome(long possiblePalindrome) {
    std::deque<int> integers;

    while (possiblePalindrome != 0) {
        integers.push_front (possiblePalindrome % 10);
        possiblePalindrome = possiblePalindrome / 10;
    }

    return isPalindrome(integers);
}


int main()
{
    long max = 0;

    for( int i = 999; i > 0; i-- ) {
        for( int j = 999; j > 0; j-- ) {
            long number = i*j;


            if(isPalindrome(number)) {
                // std::cout
                //     << i << " * " << j
                //     << "(" << number << ")"
                //     << " is a palindrome";
                // std::cout << std::endl;

                if(number > max) {
                    max = number;
                }
            } else {
                // std::cout
                //     << " is not a palindrome";
            }
        }
    }

    std::cout
        << max
        << std::endl;

    return 0;
}
