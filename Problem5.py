# Project Euler - Problem 5
# Link: https://projecteuler.net/problem=5
# Author: Josh Hess

from math import gcd

# Function to find the LCM of two numbers x and y
def lcm(x, y):
    # Formula for LCM
    return abs(x * y) // gcd(x, y)

# Function to calculate all LCM's up to n
def lcm_up_to(n):
    # Set initial LCM to 1
    lcm_result = 1
    for i in range(1, n + 1):
        lcm_result = lcm(lcm_result, i)
    
    return lcm_result

# Calculate and print solution
smallest_num = lcm_up_to(20)
print(f"The smallest positive number that's evenly divisible by all numbers 1-20 is {smallest_num}.")