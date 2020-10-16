
from random import *
# Pick a random number between 1 and 100.
x = randint(1, 100)    
print(x)


###############################################


# Average Mark Generator
sub1 = int(input("enter first mark:  "))
sub2 = int(input("enter second mark: "))
sub3 = int(input("enter third mark: "))
avg = (sub1 + sub2 + sub3) / 3

if (avg >= 50):
    print("Average Achieved")

else:
    (avg <50)
    print("Average Not Achieved")

