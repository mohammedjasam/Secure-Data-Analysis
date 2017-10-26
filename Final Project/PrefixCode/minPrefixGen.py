preSet = [] # list which stores the prefix Set
unionPreSet = [] # Takes only the commons and removes redundancies from preSet[]
starList, numList = [], []
finList = []

def joinList(l):
    return ''.join(l)

def retList(starList):
    print(starList)

def remFromList(starList, tempArray):
    if joinList(tempArray) in starList:
        starList.remove(joinList(tempArray))

# This function creates two separate lists 1. with "*" and 2. without "*"
def separateLists(unionPreSet):
    # starList = []
    # numList = []
    for x in unionPreSet:
        if '*' in list(x):
            starList.append(x)
        else:
            numList.append(x)
    return starList, numList



# This is the function which generates the minimum Prefix set
# used in the tree building process!
def minPrefix(unionPreSet):
    finList = []
    unionPreSet = sorted(unionPreSet)
    starList, numList = separateLists(unionPreSet)
    # print(starList, numList)



# This function takes the binary values of numbers in the range
# and then converts it to prefix set and appends all the values to preSet List!
def createPrefix(s, preSet):
    temp = []  # temp list to generate the Prefix Set of a binary value
    temp.append(s)
    s = list(s)
    for x in range(1, len(s) + 1):
        s[-x] = '*'
        temp.append(''.join(s))
    preSet += temp






# print(starList)

def rangeRestrict(starList):
    for s in starList[:]:
        s = list(s)
        t0 = s[:]
        t1 = s[:]
        t0 = [x.replace("*", '0') for x in list(t0)]
        t1 = [x.replace("*", '1') for x in list(t1)]
        t0 = joinList(t0)
        t1 = joinList(t1)
        # print(s, t0, t1)


        if t0 in numList:
            if t1 in numList:
                pass
            else:
                # print("Removing "+joinList(s))
                # print(t1)
                remFromList(starList, s)
        else:
            # print("Removing "+joinList(s))
            remFromList(starList, s)

    return starList

sttt = ""
def checkMaxStars(temp):
    res = ""
    global sttt

    num = 0
    for x in temp:
        x = list(x)

        if num < x.count("*"):
            num = x.count("*")
            res = joinList(x)
            sttt = res
    # if not (res == ""):
    #     return res
    # else:
    #     return sttt
    return res





def removeStars(maxStarElement):
    return joinList(list(filter(("*").__ne__, maxStarElement)))

what = []





def replaceElements(listt):
    temp = listt[:]
    global what
    # print(temp, listt)
    ele = checkMaxStars(temp) # returns element with max stars in the list
    maxStarElement = list(ele)
    if ele == "":
        what = finList + temp

    else:
        finList.append(joinList(maxStarElement))

        maxStarElement = removeStars(maxStarElement)
        length = len(list(maxStarElement))

        for element in listt[:]:
            if len(listt) == 0:
                print("Jasdhhkasdjhaskm")
                break
            else:
                if maxStarElement[:] in element[:length]:
                    listt.remove(element)






def main(finList):
    r = list(map(int, input("Enter the range space separated!\n").split()))

    for n in range(r[0], r[-1]+1):
        createPrefix('{0:010b}'.format(n), preSet)  ## This function call creates the prefix set and stores in preSet list[]
    unionPreSet = list(set(preSet))
    j = list(sorted(unionPreSet))
    minPrefix(unionPreSet)
    newList = rangeRestrict(starList)
    newList = starList + numList
    lenStar = len(starList)
    # print(starList)

    for x in range(lenStar):
        replaceElements(newList)

main(finList)
print(what)