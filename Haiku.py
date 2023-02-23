import random

def main():
    y=input("Would you like a Haiku?")

    while y!="no":

        sample=open("OneSyllable.txt")
        myString1=sample.read()
        myList1 = myString1.split()
        
        sample=open("TwoSyllable.txt")
        myString2=sample.read()
        myList2 = myString2.split()
        
        sample=open("ThreeSyllable.txt")
        myString3=sample.read()
        myList3 = myString3.split()
        
        sample=open("FourSyllable.txt")
        myString4=sample.read()
        myList4 = myString4.split()


        firstline= ("{0} {1}")
        "(firstline.format(random.choice(myList1),random.choice(myList4)))"
        L1=[random.choice(myList1),random.choice(myList4)]
        for i in L1:
            print(random.choice(L1))
        
        secondline= ("{0} {1} {2}")
        print(secondline.format(random.choice(myList1),
                                random.choice(myList4),
                                random.choice(myList2)))
        thirdline=("{0}{1}{2}")
        print(thirdline.format(random.choice(myList1),random.choice(myList2),random.choice(myList2)))
        y=input("Would you like a Haiku?(say no to stop)")
        if y==("no"):
            break

        
if __name__=="__main__":
    main()
