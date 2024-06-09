def extEuclid(a, b, previousU, previousV, PpreviousU, PpreviousV):
    global GCD

    # 몫
    Q = a // b 
    
    # 나머지
    R = a % b
    
    currentU = -Q*previousU + PpreviousU 
    currentV = -Q*previousV + PpreviousV

    #R이 GCD와 같다면 베주 항등식의 U, V를 구한 것
    if R == GCD:
        print()
        print("-------Result-------")
        print("u: " + str(currentU))
        print("v: " + str(currentV))

        #모듈러 연산에서의 값들은 모두 잉여류(0 < 값 < N-1)에 속하여야 한다.
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

#초기값 세팅
extEuclid(A, B, 0, 1, 1, 0)
