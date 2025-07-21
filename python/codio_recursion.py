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
    test_number = 27
    print(is_power(test_number))
'''
Given solution:
def is_power(num):
    if num == 2:
        return True
    elif num > 2:
        return is_power(num/2)
    else:
        return False
'''


# Write a recursive function called filter_string that takes a string as a parameter. Return 
# a string that filters out characters that are consonants.
def filter_string(input):
    vowels = ["a", "e", "i", "o", "u"]
    if len(input) == 0:
        return ""
    else:
        if input[0].lower() in vowels:
          return input[0] + filter_string(input[1:])
        else:
          return filter_string(input[1:])

if __name__ == "__main__":
    test_word = 'muSic'
    print(filter_string(test_word))

'''
Given solution:
def filter_string(string):
  def helper(char):
    vowels = ['A', 'E', 'I', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if char not in vowels:
      return ''
    else:
      return char
        
  if len(string) == 0:
    return ''
  else:
    return helper(string[0]) + filter_string(string[1:])
'''