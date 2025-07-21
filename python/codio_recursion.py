# Write a recursive function called count_by that takes an integer as a parameter. 
# Return the result of recursively counting by six as many times as the parameter.
def count_by(number):
    if number == 1:
        return 6
    else:
        return 6 + count_by(number - 1)

if __name__ == "__main__":
    test_num = 3
    print(count_by(test_num))


# Write a recursive function called recursive_math that takes an integer as a 
# parameter. Return the result of recursively multiplies the numbers. Do not 
# include 0 in your recursive calls.
def recursive_math(number):
    if number == 1:
        return 1
    else:
        return number * recursive_math(number - 1)

if __name__ == "__main__":
    test_num = 15
    print(recursive_math(test_num))