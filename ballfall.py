
from graphics import*
from Button import*
from time import*
 
def main():
   
    win = GraphWin("Environment", 500, 500)

    t=0
 
    Ball = Circle(Point(250,50), 20)
    Ball .draw(win)
 
    position = Ball.getCenter()
    y= position.getY()
 
    while y < 500 and t<2:
 
       
        Ball.move(0, 5)
        y = Ball.getCenter().getY()
        t=t+0.026
        
    while y < 500*0.89 and t>2 and t <4:
        Ball.move(0, -5)
        y = Ball.getCenter().getY()
        t=t+0.026

    while y < 500 and t>4 and t<6:

        Ball.move(0, 5)
        y = Ball.getCenter().getY()
        t=t+0.026

       
    while y < 500*0.89 and t>=6 and t <7.8:
        Ball.move(0, -5)
        y = Ball.getCenter().getY()
        t=t+0.026

if __name__ == "__main__":
    main()
