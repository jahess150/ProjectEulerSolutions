# Project Euler - Problem 7
# Link: https://projecteuler.net/problem=7
# Author: Joshua Hess

from math import log, sqrt

# For this script, we'll take advantage of the Sieve of Eratosthenes.
# First, we need to estimate the upper limit for the 10,001st prime,
# Using the Prime Number Theorem, we can calculate the 
# heuristic 10,001 * ln(10,001)
num = 10001
upper_limit = int(num * log(num)) + 50000  # Plus 50,000 for margin of error (arbitrary)

# Sieve of Eratosthenes to find nth prime
def sieve_of_eratosthenes(n):
    # Set limit based on upper_limit calculated above
    limit = upper_limit

    # Create a boolean array that will mark primes as sieve is calculated
    is_prime = [True] * (limit + 1)  # Set all numbers as prime initially
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Apply Sieve of Eratosthenes
    for i in range(2, int(sqrt(limit) + 1)):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
    
    # Extract prime numbers
    primes = [i for i, prime in enumerate(is_prime) if prime]

    # Return the nth prime
    return primes[n - 1]  # Subtract 1 since array is 0-indexed

# Print solution
print(f"The 10,001st prime number is {sieve_of_eratosthenes(10001)}.")