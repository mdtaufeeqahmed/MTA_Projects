def Fac(n):
    a=0
    p=1
    for i in range(1, n+1):
        a=a+1
        p=p*a
    print("Factorial of the number = ",p)
Fac(5)
