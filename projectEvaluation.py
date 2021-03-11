import json

def projectEVAL(truth, output):
    #Get JSON data
    data = open(truth)
    data = json.load(data)
    guess = open(output)
    guess = json.load(guess)

    total = 0
    correct = 0
    bonus = {}
    bonusTotal = {}
    for i in data:
        total += 1
        add = data[i]['signTags'] == guess[i]['signTags']
        correct += add
        #For bonus calculation
        for x in data[i]['difficultyTags']:
            if(x in bonusTotal):
                bonusTotal[x] += 1
                bonus[x] += add
            else:
                bonusTotal[x] = 1
                bonus[x] = add
    #Calculate Bonus
    extra = 0
    extraPerTag = 5/len(bonusTotal)
    for i in bonusTotal:
        extra += bonus[i]/bonusTotal[i]*extraPerTag
        
    return correct/total*100+extra

if __name__ == '__main__':
    score = projectEVAL("tags.json", "tags1.json") # replace with filename (groundtruth, prediction)
    print(score)