
#Multiple of 3 Problem Code: MULTHREE

#Consider a very long K-digit number N with digits d0, d1, ..., dK-1
#(in decimal notation;
#d0 is the most significant and dK-1 the least significant digit).
#This number is so large that we can't give it to you on the input explicitly;
#instead, you are only given its starting digits and a way to construct
#the remainder of the number.

#Specifically, you are given d0 and d1; for each i ≥ 2,
#di is the sum of all preceding (more significant) digits, modulo 10 — more formally 

#Determine if N is a multiple of 3.

# The trick is that the digits will repeat after some computation
# for example conside k = 10
# d0 = 1

# d1 = 2

# d2 = (d0 + d1 ) mod 10 = ( 1 + 2 ) % 10 = 3

# d3 = (d0 + d1 + d2) mod 10 = ( 1 + 2 + 3 ) % 10 = 6  ( 2 * (d0 + d1) mod 10)

# d4 = (d0 + d1 + d2 + d3) mod 10 = ( 1 + 2 + 3 + 6 ) % 10 = 2   ( 4* (d0 + d1) mod 10)
  
# d5 = (d0 + d1 + d2 + d3 + d4) mod 10 = ( 1 + 2 + 3 + 6 + 2 ) % 10 = 4  ( 8 * (d0 + d1) mod 10)

# d6 = (d0 + d1 + d2 + d3 + d4 + d5) mod 10 = ( 1 + 2 + 3 + 6 + 2 + 4 ) % 10 = 8   ( 6 * (d0 + d1) mod 10)

# d7 = (d0 + d1 + d2 + d3 + d4 + d5 + d6) mod 10 = ( 1 + 2 + 3 + 6 + 2 + 4 + 8 ) % 10 = 6   ( 2 * (d0 + d1) mod 10)

# The same 4 digits will get repeated continuously
# So, we need to calculate how many times the 4 digits will repeat.
# If k = 10, then we will have d0,d1,d2,d3,d4,d5,d6,d7,d8,d9.
# In this, (d3,d4,d5,d6) will repeat.
# number of times the 4 digits will repeat =  (k-3)//4
# and then we need to add the remaining 3 digits (d7,d8,d9) to our result.
# d7 = d3 , d8 = d4 and d9 = d5
# Finally, we should check whether our result is divisible by 3 or not.

#=============================================================================


for _ in range(int(input())):
    k,i,j = input().strip().split()
    d0 = int(i)
    d1 = int(j)
    if int(k) == 2:
        result = (d0+d1)
    elif int(k) > 3:
        d2 = (d0+d1) % 10
        d3 = 2 * (d0+d1) % 10
        d4 = 4 * (d0+d1) % 10
        d5 = 8 * (d0+d1) % 10
        d6 = 6 * (d0+d1) % 10
        s = (d3 + d4 + d5 + d6)
        result = (((int(k)-3) // 4) * s) + d0 + d1 + d2
        digitsleft = (int(k)-3) % 4
        if digitsleft == 1:
            result += d3
        elif digitsleft == 2:
            result += (d3+d4)
        elif digitsleft == 3:
            result += (d3+d4+d5)
    if result % 3 == 0:
        print("YES")
    else:
        print("NO")
