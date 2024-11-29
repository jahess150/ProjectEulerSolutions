# Project Euler - Problem 3
# Link: https://projecteuler.net/problem=3
# Author: Josh Hess

from math import sqrt

# Function to check if x is a prime factor of y
def is_prime_factor(x, y):
    if y % x == 0:
        # Check for any possible factors of x
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        
        # Return true if no factors found
        return True
    else:
        # If x is not a factor, it cannot be a prime factor
        return False

# Set our target number and its square root
num = 600851475143
limit = int(sqrt(num))  # Only need to check integers up to sqrt(n)

# Set initial max prime to 2 (2 is the first prime number)
max = 2

# Check for all prime factors and update max factor accordingly
for i in range(3, limit):
    if is_prime_factor(i, num):
        max = i

# Print solution
print(f"The largest prime factor of {num} is {max}.")