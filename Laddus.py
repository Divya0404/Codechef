
#Laddu Problem Code: LADDU

#You might have heard about our new goodie distribution program aka
#the "Laddu Accrual System".
#This problem is designed to give you a glimpse of its rules.
#You can read the page once before attempting the problem if you wish,
#nonetheless we will be providing all the information needed here itself.

#Laddu Accrual System is our new goodie distribution program.
#In this program, we will be distributing Laddus in place of goodies
#for your winnings and various other activities (described below),
#that you perform on our system.
#Once you collect enough number of Laddus,
#you can then redeem them to get yourself anything
#from a wide range of CodeChef goodies.

#============================================================================

for t in range(int(input().strip())):
    n, origin = input().strip().split()
    laddus = 0
    for i in range(int(n)):
        inp = input().strip().split()
        if inp[0] == "CONTEST_WON":
            laddus += 300
            if int(inp[1]) <= 20:
                laddus += (20 - int(inp[1]))
            continue
        if inp[0] == "TOP_CONTRIBUTOR":
            laddus += 300
            continue
        if inp[0] == "BUG_FOUND":
            laddus += int(inp[1])
            continue
        if inp[0] == "CONTEST_HOSTED":
            laddus += 50
            continue
    if origin == "INDIAN":
        print( laddus // 200 )
    else:
        print( laddus // 400 )
