# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format
# he first line of input contains the original string. The next line contains the substring.

# CODE STARTS HERE
----------------------------------------
def count_substring(string, sub_string):
    count = 0
    l1 = len(string) 
    l2 = len(sub_string)
    for i in range (0,l1+1-l2):
        if (string[i:i+l2]==sub_string):
            count +=1
    return count
if __name__ == '__main__':
-----------------------------------------
