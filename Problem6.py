# Project Euler - Problem 6
# Link: https://projecteuler.net/problem=6
# Author: Josh Hess

# For this script, we can take advantage of the formulas we have for the
# sum of n^2 and the sum of the first n natural numbers

# Function to return the difference of the square of sum minus the
# sum of squares
def diff_of_sums(n):
    # Calculate sum of squares
    sum_of_squares = (n * (n + 1) * ((2 * n) + 1)) // 6

    # Calculate square of sum
    square_of_sum = ((n * (n + 1)) // 2) ** 2

    # Calculate and return difference
    return square_of_sum - sum_of_squares

# Print solution
print(f"The difference betweeen the sum of the squares of the first hundred natural numbers and the square of their sum is {diff_of_sums(100)}")