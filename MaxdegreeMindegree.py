from graphics import *
import random
import time

class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)
        

    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)

    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

    def getDegree(self):
        return len(self.neighbors)

    def getName(self):
        return self.name

class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        numN = 0
        while True:
            x = random.randint(140, 740)
            y = random.randint(50, 550)
            foundNode = True
            for posX in Xpositions:
                if x - 70 < posX < x + 70:
                    for posY in Ypositions:
                        if y - 70 < posY < y + 70:
                            foundNode = False
            if foundNode:
                Xpositions.append(x)
                Ypositions.append(y)
                name = names[numN]
                N = Node(x, y, win, name)
                self.nodes.append(N)
                numN += 1

            if numN == n:
                break

        edges = 0
        while edges < e:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)
            if n1 != n2:
                if n1 not in n2.getNeighbors():
                    p1 = n1.getCenter()
                    p2 = n2.getCenter()
                    L = Line(p1, p2)
                    self.E.append(L)
                    L.draw(win)
                    edges += 1
                    n1.addNeighbor(n2)
                    n2.addNeighbor(n1)

        for node in self.nodes:
            node.draw(win)
            node.color("white")

    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()

    def getAllDegrees(self):
        for n in self.nodes:
            print(str(n.getDegree()) + " : " + n.getName())

    def maxDegree(self):
        max_degree = 0
        for node in self.nodes:
            degree = node.getDegree()
            if degree > max_degree:
                max_degree = degree
        return max_degree

    def minDegree(self):
        min_degree = float('inf')
        for node in self.nodes:
            degree = node.getDegree()
            if degree < min_degree:
                min_degree = degree
        return min_degree

