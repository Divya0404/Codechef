
#Lapindromes Problem Code: LAPIN
 
#Lapindrome is defined as a string which when split in the middle,
#gives two halves having the same characters and same frequency of
#each character. If there are odd number of characters in the string,
#we ignore the middle character and check for lapindrome.
#For example gaga is a lapindrome, since the two halves ga and ga have
#the same characters with same frequency.
#Also, abccab, rotor and xyzxy are a few examples of lapindromes.
#Note that abbaab is NOT a lapindrome.
#The two halves contain the same characters but their frequencies do not match.

#Your task is simple. Given a string, you need to tell if it is a lapindrome.

#==========================================================================

for _ in range(int(input())):
    s = input()
    s = list(s)
    m = len(s)//2
    if len(s)%2 == 0:
        s1 = s[:m]
        s2 = s[m:]
    else:
        del s[m]
        s1 = s[:m]
        s2 = s[m:]
    s1.sort()
    s2.sort()
    flag = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print('YES')
    else:
        print('NO')
