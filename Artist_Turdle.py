import turtle

class Artist:

    def __init__(self, t):
        self.t = t

    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        
    def square(self, size = 200):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)
            
    def poly(self, size = 100):
        for i in range(5):
            self.t.right(72)
            self.t.forward(size)
            
    def circle(self, size = 1):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size)
            
    def star(self, size = 100):
        for i in range(5):
            self.t.right(280)
            self.t.left(64)
            self.t.forward(size)

    
    def button(self):
        
        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(0)
        art = Artist(t)
        art.move(-150,-150)
        art.triangle()
        art.poly()
        
    def wheel(self):
        
        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(0)
        art = Artist(t)
        art.move(150,150)
        art.circle()
        art.move(205,75)
        art.star(110)
        
        


def main():

    canvas = turtle.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    art = Artist(t)
    art.move(150,200)
    art.wheel()
    art.move(-100, 200)
    art.square()
    art.move(0,0)
    art.move(150,-150)
    art.star()
    art.move(200,0)
    art.button()
    
 
        





if __name__ == "__main__":
    main()
