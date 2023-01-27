from graphics import *
from Button import *
def main():
    win = GraphWin("My window", 800, 600)
    noun= Text(Point(80,100), ("Noun"))
    noun.draw(win)
    n1= Entry(Point(200,100),15)
    n1.draw(win)

    noun2= Text(Point(150,200), ("Noun2"))
    noun2.draw(win)
    n2= Entry(Point(300,200),15)
    n2.draw(win)

    Verb= Text(Point(150,300), ("Verb"))
    Verb.draw(win)
    v= Entry(Point(300,300),15)
    v.draw(win)
    
    adj= Text(Point(150,400), ("Adjective"))
    adj.draw(win)
    a= Entry(Point(300,400),15)
    a.draw(win)

    exc= Text(Point(150,500), ("Exclamation"))
    exc.draw(win)
    x= Entry(Point(300,500),15)
    x.draw(win)


    B= Button(win,Point(600,300), Point(700,400), "cyan", "generate")
    while True:
        m=win.getMouse()
        if B.isClicked(m):
            n1=n1.getText()
            n2=n2.getText()
            v=v.getText()
            a=a.getText()
            x=x.getText()
            win.close
            win1= GraphWin("MadLib", 800, 600)
            Line= Text(Point(300,250), (n1 + " was eating a cheese sandwich with his/her friends, they were enjoying thier sandwiches until"))
            Line1= Text(Point(300,260), ("they dropped their sandwich on the yucky floor of the dining hall. They " + v +" ." ))
            Line2= Text(Point(350,270), ("They could not afford a new sandwich, " + x +". However, through the kindness of his/her heart," + n2 + " bought them a new sandwich."))
            Line.draw(win1)
            Line1.draw(win1)
            Line2.draw(win1)
if __name__ == "__main__":
    main()
