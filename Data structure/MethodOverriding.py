from math import pi

# The parent class
class Shape:
    def __init__(self, name):  # the constructor method
        self.name = name

    def area(self):
        # this method should always be overidden by the child class
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):   # standard method used by the print() function
        return self.name

# a child class derived from the parent class Shape
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")   # always call the parent's constructor
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."
    
    def __str__(self): # overrining the parent's method to hide the name
        return "I have hidden my name"


# a second child class derived from the parent class Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")   # always call the parent's constructor
        self.radius = radius

    def area(self):
        return pi*self.radius**2

# create and exercise all three classes
def overrideDemo():
    squareObj = Square(4)
    circleObj = Circle(7)
    print("Name: ",circleObj)  # should print the object's name
    print("Name: ",squareObj)  # should print the object's name
    print("Fact: ",circleObj.fact())
    print("Fact: ",squareObj.fact())
    print("Circle area is ",circleObj.area())
    txt = "Circle area is {:10.2f}"
    print(txt.format(circleObj.area()))
    #print("area is %.2f " % circleObj.area())
    #
    print(circleObj.__dir__())
    
    a = 3
    print(a.__dir__())
    

def main():
    overrideDemo()
    

if __name__ == "__main__":
    main()
    
# references
# https://realpython.com/python-formatted-output/