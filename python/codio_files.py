'''
Questions from Codio
'''
# Write a program that reads a text file and returns the number 
# of lines as well as the total number of characters in the file.
import sys

test_file = sys.argv[1]

count_line = 0
count_char = 0

with open(test_file, "r") as input:
  for line in input:
    count_line += 1
    count_char += len(line)


print(f"{count_line} lines\n{count_char} characters")


# Write a program that reads a comma delimited CSV file with 
# four columns and returns the average of each column in the file.
import sys
import csv

test_file = sys.argv[1]

average = [0.0, 0.0, 0.0, 0.0]
total = 0

with open(test_file, "r") as csvfile:
    input = csv.reader(csvfile)
    for line in input:
       column = 0
       total += 1
       for number in line:
          average[column] += float(number)
          column += 1

for number in average:
   print(number/total, end = " ")


# Write a program that reads a text file and prints the contents 
# in reverse order.
import sys

test_file = sys.argv[1]

with open(test_file, "r") as input:
    reader = input.readlines()
    pos = len(reader) - 1
    while pos >= 0:
        print(reader[pos].strip())
        pos -= 1

'''
Given solution:

import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    lines = input_file.readlines()
    lines.reverse()
    for line in lines:
        print(line)
'''


# Write a program that reads a tab delimited CSV file and prints the 
# name of the oldest person in the file.
import sys
import csv

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter='\t')
    oldest_name = None
    max_age = -1
    next(reader)
    for line in reader:
        name, age = line[0], int(line[1])
        if age > max_age:
            max_age = age
            oldest_name = name

print(f"The oldest person is {oldest_name}.")

'''
Given solution:

import sys, csv

test_file = sys.argv[1]
oldest_age = 0
oldest_name = ""

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    next(reader)
    for name, age, career in reader:
        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name
            
print("The oldest person is {}.".format(oldest_name))
'''

