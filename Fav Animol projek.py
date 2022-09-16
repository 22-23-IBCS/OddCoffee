class Dog:

    #constructor method. Needed to define how
    #the class instances are created
    def __init__(self, b, col,size,hl):
        self.size= size
        self.breed = b
        self.color = col
        self.hairlength=hl


    def getBreed(self):
        return self.breed

    def setBreed(self, b):
        self.breed = b

    def getHL(self):
        return self.hairlength

    def setHL(self, hl):
        self.hairlength = hl
        
    def getCOL(self):
        return self.color

    def setCOL(self, col):
        self.color = col


    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

def main():
    #print("Hello World")

    print("Hey welcome to the dog adoption center look at this fine doggo it is a ...")

    doge1 = Dog("breed 1 is a Husky", "brown","medium","hair 1 is long")
    b = doge1.getBreed()
    print(b)
    doge1.setBreed("breed 2 is a German shepard")
    print(doge1.getBreed())
    print(doge1.getCOL())
    print(doge1.getHL())

    doge1.setHL("hair 2 is short")
    print(doge1.getHL())



    print("Our second doggo is....")

    doge2 = Dog("Great Dane", "color 1 is grey","large"," hair 1 is short")
    b = doge2.getCOL()
    print(doge2.getBreed())
    print(doge2.getSize())
    print(doge2.getHL())
    print(doge2.getCOL())
    doge2.setCOL("color 2 is pink")
    print(doge2.getCOL())

    doge2.setHL("hair 2 is long")
    print(doge2.getHL())
    


if __name__ == "__main__":
    main()
