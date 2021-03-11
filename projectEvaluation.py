import json
#How to load JSONS and access elements
data = open("tags.json")
data = json.load(data)
guess = open("tags1.json")
guess = json.load(guess)

total = 0
correct = 0
bonus = {}
bonusTotal = {}
for i in data:
    total += 1
    add = data[i]['signTags'] == guess[i]['signTags']
    correct += add
    for x in data[i]['difficultyTags']:
        if(x in bonusTotal):
            bonusTotal[x] += add
            bonus[x] += add
        else:
            bonusTotal[x] = 1
            bonus[x] = add

extra = 0
extraPerTag = 5/len(bonusTotal)
for i in bonusTotal:
    extra += bonus[i]/bonusTotal[i]*extraPerTag
    
print(correct/total*100+extra)