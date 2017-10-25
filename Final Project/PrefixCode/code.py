# Global Variables!
preSet = [] # list which stores the prefix Set
unionPreSet = [] # Takes only the commons and removes redundancies from preSet[]
genNumList = [] # Generates the num list by replacing the bits
### ___________________________________________________________________________###
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

### ___________________________________________________________________________###
# This function is a sub function of minPrefix() which will replace the bits,
# and checks which string represents the range better!
def joinList(l):
    return ''.join(l)

def checkReplaceBitsWith0(starList, numList, l, x):
    temp = l
    temp1 = l
    for element in temp:
        t = element
        element = [x.replace("*", '0') for x in list(element)]
        if joinList(element) not in numList:
            starList.remove(joinList(t))

def checkReplaceBitsWith1(starList, numList, l, x):
    temp = l
    for element in temp:
        t = element
        element = [x.replace("*", '1') for x in list(element)]
        if joinList(element) not in numList:
            starList.remove(joinList(t))



def replaceBits0(starList, numList):
    finList = []
    for x in range(5):
        tempS = []
        for y in starList:
            if list(y).count("*") == x + 1:
                tempS.append(list(y))
        # print(starList)
        checkReplaceBitsWith0(starList, numList, tempS, x)
        # print(starList)

def replaceBits1(starList, numList):
    finList = []
    for x in range(5):
        tempS = []
        for y in starList:
            if list(y).count("*") == x + 1:
                tempS.append(list(y))
        # print(starList)
        checkReplaceBitsWith1(starList, numList, tempS, x)
        # print(starList)


### ___________________________________________________________________________###
# This is the function which generates the minimum Prefix set
# used in the tree building process!
def minPrefix(unionPreSet):
    finList = []
    unionPreSet = sorted(unionPreSet)
    separateLists(unionPreSet)

def retList(starList):
    print(starList)

def remFromList(starList, tempArray, index, param):
    # temp = tempArray
    # if param == 0:
    #     checkTillEnd0(temp, index)
    # else:
    #     checkTillEnd1(temp, index)


    if joinList(tempArray) in starList:
        starList.remove(joinList(tempArray))
                # checkTillEnd0(array, index)

    # else:
        # print(tempArray)
def checkTillEnd0(array, l):
    for x in range(l+1, len(array)):
        if not( array[x] == "*" ):
            pass
        else:
            array[x] = "1"
            # l = index
            # array[index] = "0"
            # tempArray += array[l+1:]
            remFromList(starList, array, x, 1)

def checkTillEnd1(array, l):
    for x in range(l+1, len(array)):
        if not( array[x] == "*" ):
            pass
        else:
            array[x] = "0"
            # l = index
            # array[index] = "0"
            # tempArray += array[l+1:]
            remFromList(starList, array, x, 0)

def checkBetweenList0(starList):
    param = 0
    tempX = starList

    for e in tempX:
        array = list(e)
        tempArray = array
        l = 0
        for index in range(len(array)):
            if not( array[index] == "*" ):
                pass
            else:
                array[index] = "0"
                # l = index
                # array[index] = "0"
                # tempArray += array[l+1:]
                remFromList(starList, array, index, param)
                # checkTillEnd0(array, index)
                # continue
        # checkBetweenList0(starList)



def checkBetweenList1(starList):
    param = 1
    tempX = starList

    for e in tempX:
        array = list(e)
        tempArray = []
        l = 0
        for index in range(len(array)):
            if not( array[index] == "*" ):
                pass
            else:
                array[index] = "1"
                # tempArray.append("1")
                # array[index] = "1"
                # l = index
                # tempArray += array[l+1:]
                remFromList(starList, array, index, param)
                # checkTillEnd1(array, index)
                # continue
                # break

        # checkBetweenList1(starList)
        # print(starList)

        # if joinList(l) in starList:
        #     starList.remove(joinList(l))
        #     # print(l)
        #         # print(joinList(t))
        #         #
        #         # if joinList(t) in starList:
        #         #     starList.remove(joinList(t))
        #         # else:
        #         #     pass
    # print(starList)


### ___________________________________________________________________________###
# This function creates two separate lists 1. with "*" and 2. without "*"
def separateLists(unionPreSet):
    starList = []
    numList = []
    for x in unionPreSet:
        if '*' in list(x):
            starList.append(x)
        else:
            numList.append(x)
    replaceBits0(starList, sorted(numList, reverse = True))
    replaceBits1(starList, sorted(numList, reverse = True))
    retList(starList)
    #
    # checkBetweenList0(starList)
    # checkBetweenList1(starList)
    for i in range(5):
        try:
            checkBetweenList0(starList)
            checkBetweenList1(starList)
        except:
            pass
    retList(starList)


### ___________________________________________________________________________###
"""   EXECUTION PART   """
### ___________________________________________________________________________###
# Enter the range for the prefix set
r = list(map(int, input("Enter the range space separated!\n").split()))

### ___________________________________________________________________________###
for n in range(r[0], r[-1]+1):
    createPrefix('{0:05b}'.format(n), preSet)  ## This function call creates the prefix set and stores in preSet list[]

# Now that we have the preSet of every number, we need to create minPrefix that represents the range!
unionPreSet = list(set(preSet)) # removing redundancies from preSet[]
minPrefix(unionPreSet)
# print(unionPreSet)
