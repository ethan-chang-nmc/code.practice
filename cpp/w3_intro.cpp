/*
Basic Notes:

Same basic data types as java

*/

#include <iostream>
// using namespace std; can use this

int main()
{
    int num1 = 2;
    int x = 1, y = 2, z = 3;
    std::cout << "Hello World! " << num1 + 2 << "haha\n"; // alternative std:: for namespace

    // user input
    int a;
    std::cout << "Input a number: ";
    std::cin >> a;
    std::cout << "Your number is: " << a;

    float f1 = 35e3;
    double d1 = 12E4;
    std::cout << f1 << "\n";
    std::cout << d1;
    return 0;
}