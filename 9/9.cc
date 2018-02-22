#include <iostream>

// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.

// There exists exactly one Pythagorean triplet for which a + b + c = 1000.

// Find the product abc.

int main()
{
    long max = 10000;

    for(long c = 0; c <= max ; c++)
    {
        long cSquared = c*c;

        for(long b = c; b > 0; b--)
        {
            long bSquared = b*b;

            for(long a = b; a > 0; a--)
            {
                long aSquared = a*a;

                if(aSquared + bSquared == cSquared) {
                    std::cout
                        << cSquared
                        << " is a Pythagorean triplet"
                        << " of "
                        << a
                        << " and "
                        << b
                        << std::endl;

                    if(1000 == a + b + c) {
                        std::cout
                            << c
                            << " + "
                            << a
                            << " + "
                            << b
                            << " += "
                            << a + b + c
                            << " product:  "
                            << a * b * c
                            << std::endl;

                        return 1;
                    }
                }
            }
        }
    }
}
