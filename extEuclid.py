def extEuclid(a, b, previousU, previousV, PpreviousU, PpreviousV):
    global GCD
    
    Q = a // b 
    R = a % b
    
    currentU = -Q*previousU + PpreviousU 
    currentV = -Q*previousV + PpreviousV
    
    if R == GCD:
        print()
        print("-------Result-------")
        print("u: " + str(currentU))
        print("v: " + str(currentV))
        
        if currentU < 0:
            isMMI = input("Are you tryna find the Modular Multiplicative Inverse? (Y/N): ")
            if isMMI == "Y":
                N = int(input("N: "))
                currentU = (currentU + N) % N
                print()
                print("-------Result-------")
                print("u(as an MMI): " + str(currentU))
                print("v: " + str(currentV))
            
        quit()
    
    PpreviousU = previousU 
    PpreviousV = previousV 
    
    previousU = currentU 
    previousV = currentV 
    
    extEuclid(b, R, previousU, previousV, PpreviousU, PpreviousV)
    
GCD = int(input("GCD: "))
A = int(input("A: "))
B = int(input("B: "))

extEuclid(A, B, 0, 1, 1, 0)