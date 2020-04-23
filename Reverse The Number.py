

#Reverse The Number Problem Code: FLOW007
 
#If an Integer N, write a program to reverse the given number.

#=========================================================================

for _ in range(int(input())):
    n = int(input())
    r = ''
    while n>0:
        r += str(n%10)
        n = n // 10
    print(int(r))
