import pandas as pd
import numpy as np

inven = (pd.read_csv('idlerpginventory.csv', header=None)).to_numpy()
print(inven)

class Equipment:
    identifier = ''
    stat = 0
    equipment_type = ''
    
    def __init__(self, i, s, t):
        self.identifier = i
        self.stat = s
        self.equipment_type = t
        
    def compare(self, e):
        if e.stat > self.stat: return -1
        if e.stat == self.stat: return 0
        if e.stat < self.stat: return 1
        
    def canMerge(self, e):
        return e.stat > (self.stat - 6) and e.stat < (self.stat + 6) and e.equipment_type == self.equipment_type
    
def printequipment(equipment):
    for item in equipment:
        print(str(item.identifier) + "\t" + str(item.stat) + "\t" + str(item.equipment_type))  
    print()
        
#partition for quicksort
def partition(list, low, high):
    i = low - 1
    pivot = list[high]
    
    for j in range(low, high):
        if not (list[j].compare(pivot) != -1):
            i += 1
            list[i], list[j] = list[j], list[i]
    
    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)

#quicksort
def qsort(list, low, high):
    if(low < high):
        pi = partition(list, low, high)
        qsort(list, low, pi - 1)
        qsort(list, pi + 1, high)

#check for NaN
def isNaN(n):
    return n != n

swords = []
shields = []
for i in range(0, len(inven)):
    if not isNaN(inven[i][0]):
        if(inven[i][2] == 'sword'):
            swords.append(Equipment(inven[i][0], inven[i][1], inven[i][2]))
            
        if(inven[i][2] == 'shield'):
            shields.append(Equipment(inven[i][0], inven[i][1], inven[i][2]))
            
printequipment(swords)
printequipment(shields)

qsort(swords, 0, len(swords) - 1)
qsort(shields, 0, len(shields) - 1)   

printequipment(swords)
printequipment(shields)