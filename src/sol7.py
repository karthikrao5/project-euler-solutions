import math

def SieveOfEratosthenes(n):
    listOfPrimes = []
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    
    val_to_check = 2

    while (val_to_check <= math.sqrt(n)):
        
n = 1000000

print ("Following are the prime numbers smaller")
print ("than or equal to", n)
SieveOfEratosthenes(n)
