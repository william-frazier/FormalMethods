#### BEGIN zune_program.py
#### Assaf Kfoury
#### 6 July 2019

# To run this script, issue the command:
#       >>> execfile ('zune_program.py')
# at the prompt of the Python interpreter >>>, after which you can try
# to execute the function 'daysToYear' on different inputs.

# This Python script contains what we may call the "Zune buggy function",
# which was part of the internal clock driver for the Microsoft Zune 30G
# music player. It was Microsoft's answer in 2006 to the Apple iPod, the
# portable media player which Apple started developing in 2001. The original
# Zune buggy function was written in C. It is here translated into Python
# and named 'daysToYear'. 

# You can read about Zune and its buggy function in many places on the Web.
# Check out, for example, the following websites:
# https://freedom-to-tinker.com/2009/01/12/debugging-zune-blackout/
# https://bits.blogs.nytimes.com/2008/12/31/the-day-microsoft-zunes-stood-still/
# http://bit-player.org/2009/the-zune-bug

# The function 'daysToYear' takes an integer input, assigned to the parameter
# 'days', which is a count of the number of days elapsed since January 1, 1980.
# The function is then supposed to determine the year in which the last day
# of that count occurs. For example, if 'days' is assigned 1234, then the
# function is supposed to return year 1983, because
#     year 1980 has 366 days (leap year),
#     year 1981 has 365 days (non-leap year),
#     year 1982 has 365 days (non-leap year),
#     year 1983 has 365 days (non-leap year),
# with the first three numbers adding up to 1096 days, and the first four
# numbers adding up to 1461 days, thus implying that the last day in the
# count 1234 must be a day in the year 1983.

# Before we show the original Zune implementation of the function 'daysToYear', 
# we give an implementation of the function 'isLeapYear(x)' which decides
# whether 'x' is a leap year. The year 1980 is a leap year and every 4-th
# year after 1980 is a leap year:

def isLeapYear_1 (x) :
    return ((x - 1980) % 4) == 0

# A more efficient implementation of 'isLeapYear(x)' uses the bitwise operator
# '&', based on the fact that a multiple of 4 always has '00' as its last two
# digits in its binary representation. We have to check whether the last two
# digits of 'x' are each set to '0' or not, and if they are, then the equality
# '(x & 3) == 0' is True because the binary expansion of 3 is '11':

def isLeapYear_2 (x) :
    return ((x & 3) == 0) 

def daysToYear (days) :
    year = 1980;
    while (days > 365) :
        if (isLeapYear_2 (year)) :
            if (days > 366) :
                days = days - 366
                year = year + 1
        else :
            days = days - 365
            year = year + 1
    return year

# However, this implementation of 'daysToYear' has a BUG!!! On most input
# values, it returns the correct output. For example, 'daysToYear (1234)'
# returns 1983 and 'daysToYear (1820)' returns 1984, but 'daysToYear (1827)'
# enters an infinite loop!!!

# QUESTION 1: Can you detect the flaw in the implementation of 'daysToYear'?
#
# HINT 1: The execution of 'daysToYear (days)' diverges when the number assigned
#         to the input parameter 'days' is the number of days from Jan 1, 1980,
#         to the last day of a leap year (inclusive at both ends).

# QUESTION 2: Let N be the number of days from January 1, 1980, to today's date
# (July 6, 2019). The number initially assigned to the input parameter 'days' is 
# a number in the set { 0, 1, ... , N } and program 'daysToYear' is supposed to 
# translate that number to a year in the set { 1980, 1981, ... , 2019 }. Give
# an upper bound on the expected number of iterations of the while-loop.
#
# HINT 2: Each iteration of the while-loop reduces the value stored in 'days'
#         by 365 or 366.

#### END zune_program.py
