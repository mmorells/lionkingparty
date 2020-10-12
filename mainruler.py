#!/usr/bin/env python

import json
from itertools import combinations

class Guest:
    def __init__(self, name, ruler, score):
        self.name = name
        self.ruler = ruler
        self.score = score

def openJson():
    # put json into an array
    with open('guests.json') as json_file:
        data = json.load(json_file)
        for p in data:
            if p['ruler'] is not None:
                p1 = Guest(p['name'], p['ruler'], p['party-animal-score'])
                guestArray.append(p1)
            else: 
                global ruler 
                ruler = Guest(p['name'], p['ruler'], p['party-animal-score'])

def uniqueCombs():
    namesArray = []
    scoresArray = []
    arraySum = []
    
    # put guest names in array
    for i in range(len(guestArray)):
        namesArray.append(guestArray[i].name)
    
    # find combinations of names and scores
    partyGroup = [",".join(map(str, comb)) for comb in combinations(namesArray, 3)]
    
    for j in range(len(guestArray)):
        scoresArray.append(guestArray[j].score)
    
    for comb in combinations(scoresArray, 3):
        res = sum(list(comb)) 
        arraySum.append(res)
    
    # find largest score
    index = findLargest(arraySum, len(arraySum))
    maxParty = partyGroup[index]
    splitNames = maxParty.split(',')
    print(ruler.name)
    for k in splitNames:
        print(k)

def findLargest(arr, n):
    max = arr[0] 
    index = 0
    
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
            index = i
    return index

guestArray = []
openJson()
uniqueCombs()