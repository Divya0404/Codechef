
#Carvans Problem Code: CARVANS

#Most problems on CodeChef highlight chef's love for food and
#cooking but little is known about his love for racing sports.
#He is an avid Formula 1 fan.
#He went to watch this year's Indian Grand Prix at New Delhi.
#He noticed that one segment of the circuit was a long straight road.
#It was impossible for a car to overtake other cars on this segment.
#Therefore, a car had to lower down its speed if there was a slower car
#in front of it. While watching the race,
#Chef started to wonder how many cars were moving at their maximum speed.

#Formally, you're given the maximum speed of N cars in the order
#they entered the long straight segment of the circuit.
#Each car prefers to move at its maximum speed.
#If that's not possible because of the front car being slow,
#it might have to lower its speed. It still moves at the
#fastest possible speed while avoiding any collisions.
#For the purpose of this problem, you can assume that the straight segment
#is infinitely long.

#Count the number of cars which were moving at their maximum speed
#on the straight segment.

#==========================================================================

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    c = 1
    for i in range(1,len(a)):
        if min(a[i],a[i-1]) == a[i]:
            c += 1
        else:
            a[i] = min(a[i],a[i-1])
    print(c)
