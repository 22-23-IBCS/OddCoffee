from graphics import*
from Button import*

def main():

    win = GraphWin("Character Creation", 800, 600)

    B1 = Button(win, Point(650, 50), Point(750, 125), "salmon", "Face")

    B2 = Button(win, Point(650, 150), Point(750, 225), "salmon", "Big Eyes")
    B3 = Button(win, Point(650, 250), Point(750, 325), "salmon", "Small Eyes")
    B4 = Button(win, Point(650, 350), Point(750, 425), "cyan", "Nose1")
    B5 = Button(win, Point(650, 450), Point(750, 525), "cyan", "Nose2")

    B6= Button(win, Point(550, 50), Point(650, 125), "red", "Mouth1")
    B7= Button(win, Point(550, 250), Point(600, 350), "red", "Mouth2")
    Face = Oval(Point(150, 50), Point(550, 550))
    Face.setFill("papayawhip")
    bigEye1 = Circle(Point(350, 250), 40)
    bigEye1.setFill("red")
    bigEye2 = Circle(Point(450, 250), 40)
    bigEye2.setFill("purple")
    smallEye1 = Circle(Point(350, 250), 20)
    smallEye1.setFill("green")
    smallEye2 = Circle(Point(450, 250), 20)
    smallEye2.setFill("orange")
    Nose1= Circle(Point(400, 280), 10)
    Nose1.setFill("brown")
    Nose2= Rectangle(Point(380,280),Point(410,300))
    Nose2.setFill("blue")


    Mouth1=Rectangle(Point(380,450),Point(420,350))
    Mouth1.setFill("pink")
    Mouth2=Circle(Point(400, 400), 30)
    Mouth2.setFill("white")
    Q = QuitButton(win, Point(650, 500), Point(750, 575))

    while True:
        m = win.getMouse()
        if B1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if B2.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            bigEye1.draw(win)
            bigEye2.draw(win)

        if B3.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            smallEye1.draw(win)
            smallEye2.draw(win)

            
        if B4.isClicked(m):
            Nose2.undraw()
            Nose1.undraw()
            Nose1.draw(win)
            
        if B5.isClicked(m):
            Nose1.undraw()
            Nose2.undraw()
            Nose2.draw(win)
            
        if B6.isClicked(m):
            Mouth1.undraw()
            Mouth2.undraw()
            Mouth1.draw(win)
            
        if B7.isClicked(m):
            Mouth1.undraw()
            Mouth2.undraw()
            Mouth2.draw(win)


        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
