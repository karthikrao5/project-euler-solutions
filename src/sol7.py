import math
from typing import List

def SieveOfEratosthenes(n) -> List[int]:
    print("calculating sieve for n = " + str(n))
    
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]

    val_to_check = 2

    prime[val_to_check] = True

    while (val_to_check <= math.sqrt(n)):
        for i in range(val_to_check, len(prime)):
            if i == val_to_check:
                prime[val_to_check] = True
            elif i % val_to_check == 0:
                # print ("setting " + str(i) + " to false")
                prime[i] = False

        val_to_check = next(i for i in range(2, len(prime)) if prime[i] and i > val_to_check)
        # print ("now checking: " + str(val_to_check))

    return [i for i in range(2, len(prime)) if prime[i]]



n = 1_000_000

print ("Following are the prime numbers smaller")
print ("than or equal to", n)
primes = SieveOfEratosthenes(n)

# while len(primes) < 10_000:
#     n = n * 10
#     primes = SieveOfEratosthenes(n)
#     print(primes[-20:])

print(primes[10_000])
