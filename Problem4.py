# Project Euler - Problem 4
# Link: https://projecteuler.net/problem=4
# Author: Josh Hess

# Function to check if a given string is a palindrome
def is_palindrome(string):
    # Check if string is equal to its inverse
    return string == string[::-1]

# Check all products of 3-digit integers
max_palindrome = 1  # 1 is the initial largest palindromic number
for i in range(100, 1000):
    for j in range(100, 1000):
        # Check if i * j (both 3 digit integers) is a palindromic
        if is_palindrome(str(i * j)) and i * j > max_palindrome:
            max_palindrome = i * j

# Print solution
print(f"The largest palindromic number made from the product of two 3-digit numbers is {max_palindrome}.")