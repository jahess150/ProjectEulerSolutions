# Project Euler - Problem 8
# Link: https://projecteuler.net/problem=8
# Author: Joshua Hess

# For this problem, we are going to treat the given number as a string
# and calculate the product of each 13-digit adjacent combination one-by-one
# as we iterate through the string. As long as there are no zeroes (since a
# zero would make our product zero immediately), we update the maximum
# product if it's greater than any product previously calculated.

# Store the 1000-digit number as a string
number = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

# Function to calculate the greatest product of the adjacent-digits
def greatest_product_adjacent(series, length):
    # Set initial values for iterating
    max_product = 0
    current_product = 1
    zero_count = 0

    # For all digits in the string
    for i in range(len(series)):
        digit = int(series[i])  # Get current digit

        # Multiply the new digit
        if digit == 0:
            zero_count += 1  # If zero is within length digits, product is zero
        else:
            current_product *= digit
        
        # Remove the digit that falls out of the length-digit window
        if i >= length:  # Only apply window logic once we reach the 'length' variable
            exiting_digit = int(series[i - length])
            if exiting_digit == 0:
                zero_count -= 1  # Lower amount of zeroes in length-digit window by 1
            else:
                current_product //= exiting_digit  # Divide the last digit from the product "removing" it
        
        # Update max_product ONLY if there are no zeroes in the length-digit window
        if i >= length - 1 and zero_count == 0:
            max_product = max(max_product, current_product)
    
    # Return max product 
    return max_product

# Print solution
print(f"The greatest product of 13 adjacent digits within the given number is {greatest_product_adjacent(number, 13)}")        