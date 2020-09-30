class student:

    def __init__(self, name, rollno):
        self.n=name
        self.r=rollno
        self.lap= self.laptop()
    def show(self):
        print(self.n, self.r)
        self.lap.show()             # takes the cursor to the show() of inner class

    class laptop:                   # inner class
        def __init__ (self):
            self.brand='Lenovo'   # adding the details of laptop for s1 within the inner class.
            self.cpu='kaddu'
            self.ram='baigan'
        def show(self):                             # show statement within inner class-different from the show() of outer main class
            print(self.brand, self.cpu, self.ram)


s1= student('MTA',7)                # s1 & s2 are created objects of class "STUDENT"
s2= student('AF',5)
s2.lap.brand='Masala'    # adding the details of laptop for s2 from outside the inner class.
s2.lap.cpu='DD1'
s2.lap.ram='DD2'
s1.show()                    # s1 passed as self to the class method-show()-outside the inner class
s2.show()
lap1= student.laptop()  # object created outside the inner class

