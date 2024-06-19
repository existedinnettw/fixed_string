#include "fixed_string.hpp"
#include <iostream>

using namespace std;
using namespace fixstr;

int main()
{
    using namespace fixstr;
    constexpr fixed_string first = "Hello, ";
    constexpr fixed_string second = "World!";
    constexpr auto         result = first + second; // "Hello, World!"
    cout << result << endl;
    return EXIT_SUCCESS;
}