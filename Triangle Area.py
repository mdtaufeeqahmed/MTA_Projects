# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))
a=int(input('Enter the length of 1st side: '))      # when entered directly(without using int), the values are taken as string. hence compulsory to mention 'int' to make it interger value
b=int(input('Enter the length of 2nd side: '))
c=int(input('Enter the length of 3rd side: '))
s=(a+b+c)//2;
Area= float((s*(s-a)*(s-b)*(s-c))**0.5)
print('The Area of the traingle is ', ((s*(s-a)*(s-b)*(s-c))**0.5))
print('The Area of the traingle is ', Area)
print('The Area of the traingle is %0.2f' %((s*(s-a)*(s-b)*(s-c))**0.5))
print('The area of the traingle with sides {}, {}, {} is {}'.format(a,b,c,Area))
print('The area of the traingle is %0.3f' %Area)