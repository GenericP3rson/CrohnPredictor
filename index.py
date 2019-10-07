'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
processedData = "processedData"
try:
    data = pd.read_csv(F"{processedData}.csv").values()
except:
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)


class Crohns():
    def __init__(self, parent="processedData.csv"):
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]

    def openData(self):
        li = []
        for i in self.ing:
            if (type(i) == type([])):
                li += i
        self.foodSet = set(li)
        # print(len(li), len(foodSet))
        self.foodToIng = {food: ing for food, ing in zip(self.food, self.ing)}
        self.foodToNum = {food: num for num, food in enumerate(self.foodSet)}
        self.numToFood = list(self.foodSet)
        # print(self.foodToIng["BAGELS"])
        print(len(self.foodToIng), len(self.foodToNum), len(self.numToFood))

    def enterFood(self, food, inflammed):
        results = self.findFood(food)
        if results:
            for i in results:
                inIt = False
                for j in self.ingEaten:
                    if i == j[0]:
                        if inflammed: j[1]+=1 # Adds one to inflammed
                        j[2]+=1 # Adds one to total
                        j[3] = j[1]/j[2] # Updates the %
                        inIt = True
                        break
                if not inIt:
                    if inflammed: self.ingEaten.append([i, 1, 1, 1.0])
                    else: self.ingEaten.append([i, 0, 1, 0.0])

    def findFood(self, food):
        if (not food in self.foodSet): 
            print("ERROR: "+food +" not found")
            return False
        else: 
            # print(self.foodToIng[food])
            return self.foodToIng[food]
    def mostLikely(self):
        self.ingEaten = sorted(self.ingEaten, reverse = True, key=lambda x:x[3])
    def filter(self):
        self.mostLikely()
        # print(self.ingEaten)
        num = self.ingEaten[0][3]
        # print(num)
        count = 0
        self.order = [[self.ingEaten[0]]]
        i = 1
        while i < len(self.ingEaten):
            if (self.ingEaten[i][3] == num):
                self.order[count].append(self.ingEaten[i])
            else:
                num = self.ingEaten[i][3]
                count+=1
                self.order.append([self.ingEaten[i]])
            # print(len(self.order), num)
            i+=1
            # while i < len(self.ingEaten) and self.ingEaten[i][3] == num:
            #     self.order[count].append(self.ingEaten[i])
            #     i+=1
            #     # print(self.order)
            # # i+=1
            # if not i < len(self.ingEaten):
            #     num = self.ingEaten[i][3]
            #     self.order.append([self.ingEaten[i]])
            #     count+=1
            #     i+=1
            # print(count, i, num)
        # print(self.order)
        return self.order
    def printN(self, something):
        for i in something:
            print(i)
    def printFa(self):
        for i in self.order:
            print(f"\nOCCURING {i[0][3]} TIMES:")
            print([x[0] for x in i])


i = Crohns()
i.openData()
i.enterFood("FRENCH FRIES", 0)
i.enterFood("POPCORN", 1)
i.enterFood("SPAGHETTI", 0)
i.enterFood("WHITE BREAD", 0)
i.enterFood("TOMATO", 1)
i.enterFood("MILK", 1)
i.enterFood("YOGURT", 1)
# i.mostLikely()
# i.printN(i.ingEaten)
i.filter()
i.printFa()
