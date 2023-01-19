
# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the funtion.

def hello_name():
    user_name = input("What is your name? ")
    print("Hello, " + user_name + "!")

# Question 2
# Write a python funtion, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for odds in range(101):
        if odds % 2 != 0:
            print(odds)
        
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
 
def max_num_in_list(a_list):
    return max(a_list)
    
# Question 4
# Write a function to return if the given year is a leap year.

def is_leap_year():
    a_year = input("Would you like to know what year is a leap year?\nPlease enter a year: ")    
    if int(a_year) % 4 == 0:
        print(a_year + " is a leap year.")
    else:
        print(a_year + " is not a leap year.")

# Question 5
# Write a function to check to see if all numbers in a list are consecutive numbers.
car = [1, 3, 4, 5, 2]
cars = [17, 19,20,18,21]
carss = [1,3,4,6,5]
def is_consecutive(a_list):
    sort = sorted(a_list)
    test_list = list(range(min(a_list), max(a_list) + 1))
    if len(sort) == len(test_list):
        print("This is a consecutive list.")
        return True
    else:
        print("This is not a consecutive list.")
        return False
is_consecutive(cars)