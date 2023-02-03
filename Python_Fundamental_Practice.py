import random
import math
xe=int(input("type a numberpls"))
ye=int(input("numberpls"))
ze=int(input("numberpls"))

mean=(xe+ye+ze)/3

if xe<ye and ye<ze:
    median=ye

if ze<ye and ye<xe:
     median=ye

if ze<xe and xe<ye:
    median=xe
if ye<xe<ze:
    median=xe
if xe<ze and ze<ye:
    median=ze
if ye<ze and ze<xe:
    median=ze
    
print(median)
print(mean)

me=random.randint(1,100)

if me%3==0 and me%5==0 and me%2==0:
    print(me)
    print("True")
else:
    print(me)
    print("False")
import random

numbers = [random.randint(1, 50) for i in range(10)]

maximum = max(numbers)
minimum = min(numbers)
ran = maximum - minimum

print("numbers", numbers)
print("maximum", maximum)
print("minimum", minimum)
print("range", ran)


he = int(input("Enter x coordinate: "))
je = int(input("Enter y coordinate: "))

distance = math.sqrt(he**2 + je**2)
theta = math.asin(je/distance)

print("Distance from (0, 0)", distance)
print("Angle θ:", theta, "radians")

score=0
    
L1=list["a","e","i","o","u","l","n","r","s","t"]
for i in L1:
    i=1

L2=list["d","g"]
for i in L1:
    i=2
L3=list["b","c","m","p"]
for i in L3:
    i=3
L4=list["f","h","v","w","y"]
for i in L4:
    i=3
L5=list["k"]
for i in L5:
    i=5
L6=["j","x"]
for i in L6:
    i=8
L7=["q","z"]
for i in L7:
    i=10
    
name=input("type a name")
name=name.lower()
for char in name:
    if char in (L1):
        score=score+1
    if char in (L2):
        score=score+2
    if char in (L3):
        score=score+3
    if char in (L4):
        score=score+4
    if char in (L5):
        score=score+5
    if char in (L6):
        score=score+8
    if char in (L7):
        score=score+10
    print(score)
    

