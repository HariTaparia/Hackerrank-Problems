# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .

# Input Format

# A single integer denoting .

# Constraints

# Output Format

# Print  lines where each line  (in the range ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of . Each printed value must be formatted to the width of the binary value of .

# Sample Input

# 17


----------------------
def print_formatted(number):
    # your code goes here
    sr = bin(number)
    w = len(sr[2:])
    for i in range(1,number+1):
       print(str(i).rjust(w),str(oct(i)[2:]).rjust(w),str(hex(i)[2:].upper()).rjust(w),str(bin(i)[2:]).rjust(w))

if __name__ == '__main__':
-----------------------
