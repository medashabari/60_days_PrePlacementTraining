""" 
18. Implement a decorator function called ‘timer’ that measures the execution time of a function.
 The ‘timer’ decorator should print the time taken by the decorated function to execute.
 Use the ‘time’ module in Python to calculate the execution time.

Example:

import time

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()

Output:
"Execution time: 2.00123 seconds"
"""

import time 

def timer(func):
    def wrapper():
        start_time = time.time()
        res=func()
        end_time = time.time()
        total_time = end_time - start_time
        print("Execution time : {:.5f} seconds".format(total_time))
        return res
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()


