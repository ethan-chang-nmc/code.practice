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