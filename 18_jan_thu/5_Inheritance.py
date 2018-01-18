class Person:
    def __init__(self, first, last):
        self.firstn = first
        self.lastn = last

    def Name(self):
        return self.firstn + " " + self.lastn

class Emp(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffno = staffnum

    def GetEmp(self):
        return self.Name() + " , " + self.staffno

a = Person("Alex", "Karlos")
b = Emp("Jhon", "Carter", "A103")
print(a.Name())
print(b.GetEmp())
