class student:
    var1 = 'Hello'
    def __init__(self, roll, name):
        self.r = roll
        self.n = name
        print(self.r, ' : ', self.n)

    def sample(self):
        print("this is just a sample code")


s1 = student(1, 'Alex')
s2 = student(2, 'John')
print("Data stored")
print(s1.sample())
print(s1.var1)