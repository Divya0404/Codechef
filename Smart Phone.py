
#Smart Phone Problem Code: ZCO14003
 
#Zonal Computing Olympiad 2014, 30 Nov 2013

#You are developing a smartphone app.
#You have a list of potential customers for your app.
#Each customer has a budget and will buy the app at your declared price
#if and only if the price is less than or equal to the customer's budget.


#You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.


#For instance, suppose you have 4 potential customers
#and their budgets are 30, 20, 53 and 14.
#In this case, the maximum revenue you can get is 60.

#===========================================================================

max = 0
a = []
for _ in range(int(input())):
    n = int(input())
    a.append(n)
a.sort()
l = len(a)
for i in range(len(a)):
    rev = a[i]*(l-i)
    if rev > max:
        max = rev
print(max)

