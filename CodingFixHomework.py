# IBCS "Find my error" homework!

import math

# formal greeting. get the user's name and formally say hello to them
def greet():
    name = input("What's your name?\n")
    response = "Hello, {}. It is nice to meet you".format(name)
    print(response)

# determine the area of a circle given its radius
def circleArea(r):
    if r <= 0:
        return "Invalid circle dimensions"
    else:
        return math.pi * r ** 2

# given a dictionary of students and their grades, print out which students
# need to study more (grade below 73)
def studyMore(D):
    for student, grade in D.items():
        if grade < 73:
            print(student + " needs to study more.")

# given a dictionary of students and their grades, calculate
# the mean and median of the grades. print them out
def meanMedian(D):
    listOfGrades = list(D.values())
    listOfGrades.sort()
    total = sum(listOfGrades)
    mean = total / len(listOfGrades)
    if len(listOfGrades) % 2 == 0:
        median = (listOfGrades[len(listOfGrades) // 2] + listOfGrades[len(listOfGrades) // 2 - 1]) / 2
    else:
        median = listOfGrades[len(listOfGrades) // 2]

    print("Average grade was: ", mean)
    print("Median grade was: ", median)

def main():
    D = {"Jake" : 90,
         "Betty" : 20,
         "Aristotle" : 100,
         "Genghis" : 25,
         "Shirley" : 88,
         "Salt" : 6,
         "Charlie" : 91,
         "Seacrest" : 72,
         "Ryan": 73}

    greet()
    print(circleArea(2))
    studyMore(D)
    meanMedian(D)

if __name__ == "__main__":
    main()
