def main():

    #Food store

    Gaming = {"Gaming Mouse" : 25.00,
             "Mousepad" : 5.00,
             "Gfuel" : 13.00,
              "Office Mouse" : 12.00,
              "Gfuel Bottle" : 10.00,
              "Mic" : 20.00,
              "Headphones" : 25.00,
              "Gaming Headphones" : 30.00,
             "240hzmonitor" : 400.00,
             "3070 PC" : 1500.00,
             "3080 PC" : 1800.00}
    
    print("Welcome to PC Central!")
    print(list(Gaming.keys()))
    request = input("What would you like to buy?\n")
    price = Gaming.get(request)
    many = int(input("How many would you want?\n"))
    print("Here you go!\nYou got " + str(many) + " " + request)
    print("That would be $" + str(round(price*many, 2)) + " dollars")
    total=(price*many)
    

    toBuy=[]
    while True:
        print(list(Gaming.keys()))
        request = input("What would you like to buy?\n")
        price = Gaming.get(request)
        many = int(input("How many would you want?\n"))
        print("Here you go!\nYou got " + str(many) + " " + request)
        print("That would be $" + str(round(price*many, 2)) + " dollars")
        total=total+Gaming.get(request)

        res = input("Continue shopping? Enter 'stop' if done shopping\n")
        if res == "stop":
            print("Thanks for shopping at PC Central!!!")
            toBuy.append(request)
            total=round(total)+Gaming.get(request)
            print("Your Total is $"+str(round(total)))
            break
        else:
            toBuy.append(request)
            total=round(total)+Gaming.get(request)










if __name__ == "__main__":
    main()  

