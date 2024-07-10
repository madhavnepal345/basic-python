

def isPrime(n, i=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return isPrime(n, i + 1)

def printPrimes(n):
    if n < 2:
        return
    if isPrime(n):
        print(n)
    printPrimes(n - 1)

num = int(input("Enter a number: "))

printPrimes(num)