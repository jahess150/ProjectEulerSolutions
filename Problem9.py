# Project Euler - Problem 9
# Link: https://projecteuler.net/problem=9
# Author: Joshua Hess

# Function to check whether three numbers a, b, c are a pythagorean triplet
def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

# Function to calculate the product of the pythagorean triplet equal
# to the given n
def find_triplet_product(n):
    # Since a < b < c, a must be less than n / 3
    for a in range(1, n // 3):
        # b must be less than n / 2 and be greater than a
        for b in range(a + 1, n // 2):
            # Rearrange equation a + b + c = n to calculate c
            c = n - a - b

            # If the triplet is pythagorean, return their product
            if is_pythagorean_triplet(a, b, c):
                return a * b * c

# Print solution
print(f"The product of the pythagorean triplet that sums to 1000 is {find_triplet_product(1000)}.")