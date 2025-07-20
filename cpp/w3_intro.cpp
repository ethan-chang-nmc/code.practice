/*
Basic Notes:

Same basic data types as java, must import string library

*/

#include <iostream>
#include <string>
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

    //testing e (power 10)
    float f1 = 35e3;
    double d1 = 12E4;
    std::cout << f1 << "\n";
    std::cout << d1;
    return 0;

    // testing string
    std::string test = "Hello";
    
    // creating auto variables - once assigned it stays the same
    auto myNum = 5; // int
    auto myFloatNum = 5.99; // float
    auto myDoubleNum = 9.98; // double
    auto myLetter = 'D'; // char
    auto myBoolean = true; // bool
    auto myString = std::string("Hello"); // std::string

    // incrementing/decrememnting
    int x = 5;
    ++x; // --
    std::cout << x;
}