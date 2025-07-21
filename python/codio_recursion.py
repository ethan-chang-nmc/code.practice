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


# Write a recursive function called list_math that takes a list of non-zero integers 
# as a parameter. Return the recursive sum for the numbers in the list.
def list_math(input):
    if len(input) == 1:
        return input[0]
    else:
        new_list = input[:-1]
        return input[-1] + list_math(new_list)

if __name__ == "__main__":
    test_list = [14, 20, 7, 2]
    print(list_math(test_list))
'''
Given solution:
def list_math(lst):
          if len(lst) == 1:
            return lst[0]
          else:
            return lst[0] + list_math(lst[1:])
'''


# Write a recursive function called is_power that takes an integer as a parameter. Return 
# a boolean that indicates if the parameter is a power of two.
def is_power(number):
    if number == 1:
        return True
    elif number < 1:
        return False
    else:
        return is_power(number/2)
    
if __name__ == "__main__":
    example_number = 27
    print(is_power(example_number))