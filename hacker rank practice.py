def is_leap(year):
    # Check if the year is divisible by 400
    if year % 400 == 0:
        return True
    # Check if the year is divisible by 100 but not 400
    elif year % 100 == 0:
        return False
    # Check if the year is divisible by 4 but not 100
    elif year % 4 == 0:
        return True
    # If none of the above, it's not a leap year
    else:
        return False
    
year=int(input("enter "))
print(is_leap(year))

#confusing questions

#binary width and string formatting method







# #Given an integer, , print the following values for each integer  from  to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print
# Prints

# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

# Input Format

# A single integer denoting .

# Constraints

# Sample Input

# 17
# Sample Output

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001



#binary width and string formatting method

def print_formatted(number):
    # Determine the width of the binary representation of 'number'
    width = len(bin(number)) - 2  # The bin() function adds a '0b' prefix, so subtract 2
    
    # Loop through each number from 1 to 'number'
    for i in range(1, number + 1):
        # Print the decimal, octal, hexadecimal (capitalized), and binary
        # Each value is right-aligned with the width of the binary representation
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



