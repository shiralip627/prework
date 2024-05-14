# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):

def hello_name(user_name):
    """Setting up the function to print 'hello_' + the input."""
    print("hello_" + user_name + "!")
hello_name('USERNAME')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
# def first_odds():

def first_odds(n):
    """Write a return statement for x in a specefic range that only returns odd numbers."""
    return [x for x in range(0,100) if x % 2 != 0]
print(first_odds(100))

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
# def max_num_in_list(a_list):

a_list = [5, 10, 15, 20, 25]

def max_num_in_list(a_list):
    """Use max() to find the maximum value in your list."""
    print(max(a_list))
max_num_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
# def is_leap_year(a_year):

def is_leap_year(a_year):
    """Define the Boolean value."""
    leap = False
    """Write an if statement if the year is divisible by 4, but not 100 yielding that the year is a leap year, etc."""
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        leap = True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap = False
    elif (a_year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap
print(is_leap_year(2020))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):

def is_consecutive(a_list):
    """Define the Boolean value."""
    consecutive = True
    if len(a_list) < 1:
        return False
    min_value = min(a_list)
    max_value = max(a_list)
    if max_value - min_value + 1 == len(a_list):
        return True
    else:
        return False
a_list = a_list.sort()
a_list = [2, 4, 3, 6]
print(is_consecutive(a_list))