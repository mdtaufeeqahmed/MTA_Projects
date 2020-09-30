def fact(n):
     p=1
     for i in range(1,n+1):
        p=p*i
     print("Factorial of the number within function = ", p)
     return p
result = fact(5)
print("Factorial of the number using return value = ",result)