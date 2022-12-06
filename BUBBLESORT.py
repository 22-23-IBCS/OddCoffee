import random

def main():
    randomlist = []
    for i in range(0,8):
        n = random.randint(1,3000)
        randomlist.append(n)
    print(randomlist)


    L = randomlist
    L.sort()
    print(L)

if __name__ == "__main__":
    main()
