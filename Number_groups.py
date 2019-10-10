# The positive odd numbers are sorted in ascending order as , and grouped as  and so on.

# Thus, the first group is , the second group is , the third group is , etc. In general, the  group contains the next  elements of the sequence.

# Given , find the sum of the elements of the  group. For example, for , the answer is :

# image
# ##Rationale - As you see that each term is forming a pattern in terms of cube(k) or you can form the equation that kth term will have (n+1)*n th ending terms then k-1 th term has n*(n-1) th ending term and we know that sum of odd terms form a sequence of square so going by that we can sum like this and answer is (n*(n+1))*(n*(n+1))-(n*(n-1))*(n*(n-1))
-------------------------------------

import math
import os
import random
import re
import sys

# Complete the sumOfGroup function below.
def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    return k**3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input())

    answer = sumOfGroup(k)

    fptr.write(str(answer) + '\n')

    fptr.close()
 -------------------------------------
