import random

def genLine(syl, val, excluded_letters):
    line = ""
    while True:
        v = random.randint(1,4)
        if val - v >= 0:
            myList = syl.get(v).split()
            word = random.choice(myList)
            if not any(letter in excluded_letters for letter in word):
                line += word + " "
                val -= v
        if val == 0:
            break
    
    return line

def main():
    y=input("would you like a haiku?(no to stop):")
    if y!=("no"):
        
        f1 = open("oneSyllable.txt")
        f2 = open("twoSyllable.txt")
        f3 = open("threeSyllable.txt")
        f4 = open("fourSyllable.txt")
        readOne = f1.read()
        readTwo = f2.read()
        readThree = f3.read()
        readFour = f4.read()
        syl = {1 : readOne,
               2 : readTwo,
               3 : readThree,
               4 : readFour}

        while True:
            excluded_letters = input("Enter letters you don't want in the haiku (or type skip to continue): ")
            if excluded_letters == "":
                
                print(genLine(syl, 5, excluded_letters))
                print(genLine(syl, 7, excluded_letters))
                print(genLine(syl, 5, excluded_letters))

            else:
                print(genLine(syl, 5, excluded_letters))
                print(genLine(syl, 7, excluded_letters))
                print(genLine(syl, 5, excluded_letters))
            y=input("would you like a haiku?(no to stop):")
            if y==("no"):
                print("Thank you for using my generator")
                break

if __name__ == "__main__":
    main()

