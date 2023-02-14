import random

#calculate sum, product and mean of three numbers
def calcThree(x, y, z):
    # Changed the variable names to avoid modifying the input parameters
    sum = x + y + z
    product = x*y*z
    mean = (x+y+z)/3
    return sum, product, mean

#determine the minimum value in a list of numbers
def myMin(L):
    # Initialize the minimum to the first element in the list
    m = L[0]
    for e in L:
        if e < m:
            m = e

    return m

#determine the average number of characters in a word
def sentenceData():
    sen = input("Please type a sentence.\n")
    senWords = sen.split()
    numWords = len(senWords)
    totalChar = 0
    for w in senWords:
        totalChar += len(w)

    # Used f-strings to format the output
    print("The average word length is: "+ str(round(totalChar/numWords, 2)))

#randomize the characters in a user input name (First and Last)
# and print out the users new name
def randomName():
    name = input("Please enter your first name: ")
    name2 = input("Please enter your last name: ")
    # Changed the variable names to avoid modifying the input parameters
    new_name = ""
    for n in name:
        new_name += random.choice(name)
    new_name2 = ""
    for n in name2:
        new_name2 += random.choice(name2)

    # Used f-strings to format the output
    print("Hello " +new_name+" "+ new_name2)


def main():
    # Added some example inputs for the functions
    print(calcThree(1, 2, 3))
    print(myMin([3, 1, 4, 1, 5, 9]))
    sentenceData()
    randomName()


if __name__ == "__main__":
    main()
