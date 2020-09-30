x=7
print(x)
id(x)
print(id(x))
y=8
print(id(y))
z=7
print('x=',x,'z=',z)
print(id(x),id(z))       # same address if the different variables have same value
z=9
print('x=',x,'z=',z)     # different address if the different variables have  =different values
print(id(x),id(z))
