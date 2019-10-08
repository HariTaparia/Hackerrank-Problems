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


-------------------------
def print_rangoli(size):
    # your code goes here
    w = 4*size-3
    
    for i in range (0,size):
            p1 = [str(chr(96+size-j)) for j in range (0,i)]
            p2 = [str(chr(96+size-j)) for j in range (i,-1,-1)]
            p1 = p1+ p2
            print(str('-'.join(p1)).center(w,'-'))
    for i in range (size-2,-1,-1):
            p1 = [str(chr(96+size-j)) for j in range (0,i)]
            p2 = [str(chr(96+size-j)) for j in range (i,-1,-1)]
            p1 = p1+ p2
            print(str('-'.join(p1)).center(w,'-'))

if __name__ == '__main__':
--------------------------
