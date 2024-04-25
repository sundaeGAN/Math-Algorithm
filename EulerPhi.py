def findPrimeFactors(N):
    primeFactors = []
    
    i = 2
    while i <= N:
        result = N % i

        if result == 0:
            N = N / i
            if i not in primeFactors:
                primeFactors.append(i)
            i = 2
            
        else: i += 1
    
    return primeFactors

def eulerPhi(N, primeFactorsList):
    coprimes = N
    for i in primeFactorsList:
        coprimes *= 1 - 1/i
    
    return coprimes

N = int(input("N: "))

primeFactorList = findPrimeFactors(N)
coprimes = eulerPhi(N, primeFactorList)
print("The Number of integers that are coprimes with %d between 1 and %d: %d" %(N, N-1, int(coprimes)))