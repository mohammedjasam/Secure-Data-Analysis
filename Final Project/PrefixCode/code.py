# Global Variables!
preSet = [] # list which stores the prefix Set
unionPreSet = [] # Takes only the commons and removes redundancies from preSet[]

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

# This function is a sub function of minPrefix() which will replace the bits,
# and checks which string represents the range better!
def replaceBits(starList, numList):
    finList = []
    hi = numList[0]
    low = numList[-1]

    # print(starList, numList)


# This is the function which generates the minimum Prefix set
# used in the tree building process!
def minPrefix(unionPreSet):
    finList = []
    unionPreSet = sorted(unionPreSet)
    separateLists(unionPreSet)

def separateLists(unionPreSet):
    starList = []
    numList = []
    for x in unionPreSet:
        if '*' in list(x):
            starList.append(x)
        else:
            numList.append(x)
    replaceBits(starList, sorted(numList, reverse = True))



""" -------------------------------------------------------------------------------------"""
"""   EXECUTION PART   """

# Enter the range for the prefix set
r = list(map(int, input("Enter the range space separated!\n").split()))


for n in range(r[0], r[-1]+1):
    createPrefix('{0:05b}'.format(n), preSet)  ## This function call creates the prefix set and stores in preSet list[]

# Now that we have the preSet of every number, we need to create minPrefix that represents the range!
unionPreSet = list(set(preSet)) # removing redundancies from preSet[]
minPrefix(unionPreSet)
# print(unionPreSet)
