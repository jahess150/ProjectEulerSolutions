# Project Euler - Problem 1
# Link: https://projecteuler.net/problem=1
# Author: Josh Hess

# Holds sum of all divisible naturals
sum = 0

# If a natural is divisible by 3 or 5, add it to sum
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

# Print solution
print(f"The sum of all multiples of 3 or 5 for all naturals less than 1000 is {sum}.")