# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Input Format

# The first line contains a string, .
# The second line contains the width, .

# Constraints

# Output Format

# Print the text wrapped paragraph.

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

------------------------
import textwrap

def wrap(string, max_width):
    ou = []
    for i in range(0,len(string)//max_width+1):
        ou.append(string[max_width*i:max_width*(i+1)])
    string = "\n".join(ou)
    return string

if __name__ == '__main__':
------------------------
