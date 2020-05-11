# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def smallest(val):
    for i in range(1, 21):
        if (val % i != 0):
            return False
    return True


num = 1
while True:
    if(smallest(num)):
        print(num)
        break
    else:
        num += 1

