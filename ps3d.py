from string import *
def subStringMatchExact(target, key):
    matches = []
    startPosition = 0
    matchPosition = 0
    while (matchPosition > -1):
        matchPosition = target.find(key,startPosition)
        startPosition = matchPosition + 1
        matches.append(matchPosition)
    return tuple(matches[:-1])

def constrainedMatchPair(firstMatch, secondMatch, length):
    filterMatch1 = ()
    for fM in firstMatch:
        for sM in secondMatch:
            if fM + length + 1 == sM:
                filterMatch1 = filterMatch1 + (fM,)
                break
    return filterMatch1        
    
def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print('breaking key ' + key + ' into ' + key1 + ' '+ key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print('match1: ' + str(match1))
        print('match2: ' + str(match2))
        print('possible matches for ' + key1 +  ' , ' + key2 + ' start at ' + str(filtered))
        print('---------------------')
    return tuple(set(allAnswers))
        

def subStringMatchExactlyOneSub(target,key):
    exactMatch =  subStringMatchExact(target, key)
    atMostOneMissMatch = subStringMatchOneSub(key,target)
    return tuple(set(atMostOneMissMatch) - set(exactMatch))
    


        
    
