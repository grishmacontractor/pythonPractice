class super (object) :

    def implicit(self):
        print("super class with implicit function")

class sub(super) :
    pass

superObj = super()
subObj = sub()

superObj.implicit()
subObj.implicit()
