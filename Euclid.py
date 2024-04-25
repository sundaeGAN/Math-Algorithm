def euclid(a, b):
    if a == 0:
        print(b)
        quit()
        
    elif b == 0:
        print(a)
        quit()
        
    rem = a % b
    euclid(b, rem)
    
A = int(input("A: "))
B = int(input("B: "))
    
euclid(A, B)