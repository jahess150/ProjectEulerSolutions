# Project Euler - Problem 2
# Author: Josh Hess

# Hold the sum of all even fibonacci elements
sum = 0

# While fibonacci elements are less than or equal to than 4 million
a, b = 1, 1
while b <= 4000000:
    # Add value to sum if it's even
    if b % 2 == 0:
        sum += b
    
    # Continue fibonacci sequence
    a, b = b, a + b

# Print solution
print(f"The sum of all even fibonnaci elements is {sum}.")