def search(s,e):
    answer = None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print(str(answer) + ' , ' + str(numCompares))

def bsearch(s,e, first, last): # binary search
    print(str(first) + ' , '  + str(last))
    if (last - first) < 2:
        return s[first] == e or s[last] == e
    min = first + (last - first) / 2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1)
    return besearch(s, e, mid+1, last)

def search1(s,e):
    print bsearch(s, e, 0, len(s)-1)
    print 'Search complete'

#def testSearch():
#    s = range(0,1000000)
#    raw_input('basic', -1)
#    print search(s, -1)
#    raw_input('binary', -1)
#    print search1(s, -1)


