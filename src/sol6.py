
squareSum = 0
sumSquare = 0

sumSquare = sum(range(1, 101))**2
squareSum = sum([x**2 for x in range(1, 101)])

print (sumSquare - squareSum)
