from string import *
def countSubStringMatch(target, key):
    count = -1
    startPosition = 0
    matchPosition = 0
    while (matchPosition > -1):
        matchPosition = target.find(key,startPosition)
        startPosition = matchPosition + 1
        print("find matching at: " + str(matchPosition))
        count = count + 1
    return count
        

def countSubStringMatchRecursive(target, key):
    matchPosition = target.find(key)
    if matchPosition < 0:
        return 0
    else:
        newTarget = target[matchPosition+1:]
        return 1 + countSubStringMatchRecursive(newTarget, key)
        
    
