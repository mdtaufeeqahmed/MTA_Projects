def fibanocci(length):
     a=0
     b=1

     if length <=0 :
         print("Invalid Input")
     elif length == 1:
             print('0')
     else :
         print(a,b,end=" ")
         for i in range(1,length-1,1):
              c=a+b;
              a=b;
              b=c;
              print(c,end=" ")
     print("\n")

fibanocci(7)
fibanocci(1)
fibanocci(-3)
fibanocci(25)


