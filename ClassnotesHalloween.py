import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

    
def greedyPath(m, num):
    bestHouses = []
    for i in range(5):
        for j in range(5):
            houses.append([m[i][j],[i,j]])
    for i in range (25):
        maxHval=0
        maxHcoord=[0,0]
        for h in houses:
            if h[0]>=maxHval:
                maxHval=h[0]
                maxHcoord=h[1]
        bestHouses.append(houses.pop(maxHcoord))


    
    #sort the houses in terms of best to worst
    

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #using a new starting position
    #return once a fair path is generated
    #if no fair path found, return list of zeros as coordinates
    for i in range(bestHouses):
        p = []



        #keep track of the value of the path
        #pick the next best house to start with

        


        #add neighbors to the path after comparing to see which neighbor is best
    for i in range(num-1):
            
            #check to see if we are stuck. If we get stuck, break


            
            #check all possible neighbors. Choose the best neighbor
            #add it to the path and add to the value



            #if path is complete, return path and path value

        x=random.randint(0,4)
        y=random.randint(0,4)
        p.append([x,y])
        pVal=m[x][y]
        



        return pVal, p

def randPath(m, num):
    #create an empty path
    p = []

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []
        

        #keep track of the value of the path
        #choose a random coordinate to start at

        x = random.randint(0,4)
        y = random.randint(0,4)
        p.append([x,y])

            
        pVal=m[x][y]

        

        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        #print(p)
        for i in range(num - 1):
            bad = []

            neighbors=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
            for n in neighbors:
                if (n[0]>4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1]>4) or (n[1] < 0):
                    bad.append(n)
                if n in p:
                    bad.append(n)
            #print(bad)
            #print(neighbors)
            for b in bad:
                neighbors.remove(b)
            
                if len(neighbors) == 0:
                    break


            if len(neighbors) == 0:
                    continue
            
               
            randN=random.choice(neighbors)

            

            p.append(randN)
            x=randN[0]
            y=randN[1]
            
            pVal=pVal+m[x][y]
                #choose a random direction and attempt to add the neighbor
                #do not add the neighbor to the path if it is outside of the 5x5
                #or if the neighbor is already in the path
                #break the while loop if it was a successful addition or if stuck
                
    return pVal, p
                        
                
  
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 


    num = int(input("How many houses?\n"))


  
    
    ''' Greedy Path Call '''
    #pVal, p = greedyPath(m, num)

    #print(p)



    ''' Random Path Call '''
    #calculate the average rating of a house in the neighborhood
    total=0
    for i in range(5):
        for j in range(5):
            total = total+m[i][j]
    average=total/25
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.

    pVal,p = randPath(m,num)
    while (average > pVal/num):
        pVal,p = randPath(m,num)

    print(p)
    print("The average value of the houses is "+str(average))
    print("The average value of your route is "+str(pVal/num))
            

        

if __name__ == "__main__":
    main()
