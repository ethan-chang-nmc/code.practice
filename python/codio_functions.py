# Write a function called avg that takes two parameters. Return the average of these two parameters. 
# If the parameters are not numbers, return the string, Please use two numbers as parameters
def avg(num1, num2):
    try:
        average = (num1 + num2)/2
        return(average)
    except TypeError:
        return("Please use two numbers as parameters")


# Write a function called odds_or_evens that takes a boolean and a list of integers as parameters. 
# If the boolean parameter is True, return a list of only even numbers. 
# If the boolean parameter is False, return a list of only odd numbers.
def odds_or_evens(torf, ilist):
    output = []
    if torf == True:
        for number in ilist:
            if number % 2 == 0:
                output.append(number)
    else:
        for number in ilist:
            if number % 2 != 0:
                output.append(number)
    return output
'''
Given Solution: extract common one, if bool you can just type if bool for true check
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
      if my_bool:
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(num)
                
    return return_list
'''


# Write a function called search_list that takes a list and a search term as parameters. If the 
# search term is located in the list, return the index of the matching element. The function should 
# work even if there is a difference in capitalization. If the search term is not in the list, return -1.
def search_list(input, search):
    for index, word in enumerate(input):
        if search.lower() == word.lower():
            return index
    return -1
'''
Given solution: used .index instead, does have to hold each index for words we don't care about

def search_list(lst, term):
    """Search for item in a list
    Return the index if found
    Return -1 if not found"""
    for item in lst:
        if item.lower() == term.lower():
            return lst.index(item)
    return -1
'''


# Write a function called best_team that takes a csv file as a parameter. Read the comma-delimited CSV file 
# specified by the variable mlb_data. The CSV file has a list of all of the MLB teams and their performance from 
# the 2019 season. The function should return the team name for the team with the most wins. Important, the CSV file 
# has a header of Tm,Lg,G,W,L, which stands for team name, league, games played, wins, and losses. Below are the file name and file path variables you will need for this exercise.
import csv

def best_team(input_csv):
    most_wins = -1
    team = ""
    with open(input_csv, "r") as input:
        reader = csv.reader(input)
        next(reader)
        for name, league, games, wins, losses in reader:
            wins = int(wins)
            if wins < most_wins:
                most_wins = wins
                team = name
    return team
            
