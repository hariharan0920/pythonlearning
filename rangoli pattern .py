# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------
# The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

# Function Description

# Complete the rangoli function in the editor below.

# rangoli has the following parameters:

# int size: the size of the rangoli
# Returns

# string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
# Input Format

# Only one line of input containing , the size of the rangoli.

# Constraints


# Sample Input

# 5
# Sample Output

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# Approach:

# The pattern for each row will have the letters decrementing from the corresponding letter (e.g., 'e' for size 5) down to 'a', and then incrementing back to the corresponding letter.
# The number of letters and hyphens needs to be adjusted for each row to maintain symmetry.
    
# Explanation:

# Alphabet String: We use string.ascii_lowercase to access the lowercase English alphabet.
# Rangoli Construction:
# For each row i, we slice the alphabet to get the letters from the current size down to 'a', then reverse back up to the size letter. This gives us the string of letters needed for that row.
# We join the letters with '-' to match the required format.
# The center function ensures that each row is centered, and the total width is calculated as 4*size - 3, which accounts for both the letters and the hyphens.
# Mirroring: After constructing the upper half of the rangoli (which includes the middle row), we mirror it by reversing the list and concatenating it with the rest (excluding the middle row).

# How the Code Works:

# For size = 5, the largest letter is e. Each row is constructed from e down to the corresponding letter and back up. The rows are centered and aligned using hyphens.
# The rangoli is symmetric, with the middle row having the full sequence from e to a and back to e. The rows above it progressively shrink in size.


def print_rangoli(size):
    # Get the alphabet in reverse order
    import string
    alpha = string.ascii_lowercase

    # Create the list to store each row
    result = []
    
    # Build the rangoli line by line
    for i in range(size):
        # Get the slice of letters to use for the current row
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        # Center the string with the appropriate width
        result.append(s.center(4*size - 3, '-'))
    
    # Join the upper part and lower part to form the rangoli
    print('\n'.join(result[::-1] + result[1:]))

# Example usage
n = int(input())
print_rangoli(n)