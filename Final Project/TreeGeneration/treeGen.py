import math
from functools import reduce

# This is the main function which takes the list and breaks it into two sublists based on algorithm!
def superMain(SNum, Bits):
    sub1, sub2  = [], [] # Final two sublists!
    preSet = [] # This will contain the prefix families of individual binary element
    dPreSet = {} # This stores all (key, value) pairs of (binary, prefix family)
    binRange = []
    bitLen = Bits
    dNumToBin = {} # Helper dict to convert Number to Binary
    dBinToNum = {} # Helper dict to convert Binary to Number
    S, S1, S2, L = [], [], [], [] # Important Variables of the algorithm!
    string = '{0:0' + str(bitLen) + 'b}' # static BitLength

    # Converts the numeric to binary values!
    for n in SNum:
        bNum = string.format(n)
        S.append(bNum)
        dNumToBin[n] = bNum # Adds Binary value to Number key

    for x in SNum:
        dBinToNum[dNumToBin[x]] = x # Adds Number value to Binary key

    def createPrefix(s, preSet):
        savedS = s # Copy of the S
        temp = []  # temp list to generate the Prefix Set of a binary value

        temp.append(s)

        s = list(s)
        for x in range(1, len(s) + 1):
            s[-x] = '*'
            temp.append(''.join(s))
        dPreSet[savedS] = temp # Saves the prefix family to the binary key!
        preSet += temp

        return preSet

    for element in S:
        createPrefix(element, preSet)

    # for k, v in dPreSet.items():
    #     print(k, v)

    pastLCP = [] # This list keeps track of the past Longest common prefix.
    def checkLCP(S, pastLCP):
        LCP = ""
        prefixF = []

        for i in range(len(S)):
            prefixF.append(dPreSet[S[i]])

        # Finds the intersection between prefix families of the subset
        LCP = list(reduce(set.intersection, [set(item) for item in prefixF]))

        # Checking if the current LCP is unique by removing the redundant LCP by comparing it to PastLCP
        for x in LCP:
            if x in pastLCP:
                LCP.remove(x)

        pastLCP += LCP # Adding the unique LCP to the pastLCP list for futher comparision

        ## The below block finds the Longest Common Prefix by checking for least number of * in it.
        c = 0
        countL = []

        for x in LCP:
            countL.append((x.count("*"), x))

        LCPrefix = min(countL)[1]

        LCP0 = list(LCPrefix)
        LCP1 = list(LCPrefix)

        # Replaces the first star with 0 or 1 to divide the elements of S to S1 and S2
        for x in range(len(LCP0)):
            if LCP0[x] == "*":
                LCP0[x] = "0"
                break

        for x in range(len(LCP1)):
            if LCP1[x] == "*":
                LCP1[x] = "1"
                break

        LCP0 = "".join(LCP0)
        LCP1 = "".join(LCP1)

        L0 = [] # Empty lists which will be filled by elements which have 0 in the location of the first *
        L1 = [] # Empty lists which will be filled by elements which have 1 in the location of the first *

        for i in range(len(S)):
            prefixFamily = dPreSet[S[i]] # Pulling the prefix family of individual element

            # Checking if that prefix family has LCP0 or LCP1, if present then we add to corresponding L0/L1
            if LCP0 in prefixFamily:
                L0.append(S[i])
            else:
                L1.append(S[i])

        return L0, L1 # returns the two subsets for further computation


    pastS3LCP = [] # This list keeps track of the past Longest common prefix.
    def checkS3LCP(S, pastS3LCP):
        LCP = ""
        prefixF = []

        for i in range(len(S)):
            prefixF.append(dPreSet[S[i]])

        # Finds the intersection between prefix families of the subset
        LCP = list(reduce(set.intersection, [set(item) for item in prefixF]))

        # Checking if the current LCP is unique by removing the redundant LCP by comparing it to PastLCP
        for x in LCP:
            if x in pastS3LCP:
                LCP.remove(x)

        pastS3LCP += LCP # Adding the unique LCP to the pastLCP list for futher comparision

        ## The below block finds the Longest Common Prefix by checking for least number of * in it.
        c = 0
        countL = []

        for x in LCP:
            countL.append((x.count("*"), x))

        LCPrefix = min(countL)[1]

        # Replaces the first star with 0 and 1
        LCP0 = list(LCPrefix)
        LCP1 = list(LCPrefix)

        # Replaces the first star with 0 or 1 to divide the elements of S to S1 and S2
        for x in range(len(LCP0)):
            if LCP0[x] == "*":
                LCP0[x] = "0"
                break

        for x in range(len(LCP1)):
            if LCP1[x] == "*":
                LCP1[x] = "1"
                break

        LCP0 = "".join(LCP0)
        LCP1 = "".join(LCP1)

        L0 = [] # Empty lists which will be filled by elements which have 0 in the location of the first *
        L1 = [] # Empty lists which will be filled by elements which have 1 in the location of the first *

        # Checking if that prefix family has LCP0 or LCP1, if present then we add to corresponding L0/L1
        for i in range(len(S)):
            prefixFamily = dPreSet[S[i]]
            if LCP0 in prefixFamily:
                L0.append(S[i])
            else:
                L1.append(S[i])

        return L0, L1 # returns the two subsets for further computation

    # A type of overloaded function which prints the values as required by the algorithm
    def printTheNumbers(L):
        temp1 = L[0]
        temp2 = L[1]
        temp1 = [dBinToNum[x] for x in temp1]
        temp2 = [dBinToNum[x] for x in temp2]

        # Checks which list is bigger, keeps the bigger list in temp1 and smaller in temp2
        if len(temp1) >= len(temp2):
            pass
        else:
            # Swaps if temp1 is smaller than temp2
            temp = temp1[:]
            temp1 = temp2[:]
            temp2 = temp[:]

        return temp1, temp2 # Returns the results

    n = len(S) # Length of the main S

    # This function goes over List L and checks if there is a possibility of combining two lists
    # and still satisfy the condition of being less than or equal to the half of the initial List!
    def checkCombo(L):
        i = -1 # default value
        j = -1 # default value

        for x in range(len(L)-1):
            for y in range(x + 1, len(L)):
                if (len(L[x]) + len(L[y])) <= math.ceil(n/2):
                    i = x
                    j = y
        return i, j

    # A sub main function which runs the algorithm
    def main(S, pastLCP, pastS3LCP):

        global sub1, sub2 # Stores the result.

        # This while splits the S ==> (S1, S2)
        while (len(S) > math.ceil(n/2)):
            S1, S2 = checkLCP(S, pastLCP)

            if len(S1) >= len(S2):
                L.append(S2)
                S = S1
            else:
                L.append(S1)
                S = S2

        L.append(S)

        # Checks if there are any sublists which can be combined, if they can then they will be combined
        while (checkCombo(L)):

            i, j = checkCombo(L) # Gets the index of the sublists which can be combined

            # Checking for default value, if so then we stop the combination process as there
            # are no sublists that can be combined!
            if i == -1 or j == -1:
                break

            # Copies the sublists to a and b
            a = L[i]
            b = L[j]

            Lij = L[i] + L[j] # Combining the two lists in temporary Lij
            tempD = {}

            del L[i] # Deleting the first sublist at index i

            # Deleting the second sublist at index j-1 as i has been deleted in the previous statement
            # so the index of j decreases by 1
            del L[j-1]

            L.append(Lij) # Adding the temporary combined L[i] and L[j]

        # If there are only 2 sublists after the previous step then we return the result
        if len(L) == 2:
            sub1, sub2 = printTheNumbers(L)
            return sub1, sub2 # two sublists which are the final result are returned
        else:

            pickS3List = [] # Stores the intersection and sublists as a tuple from which S3 is picked

            # Find S3 via finding the subset who's prefix families share the least number of prefixes!
            for subset in L:
                preFamilies = []
                for x in subset:
                    preFamilies.append(dPreSet[x])
                interSection = list(reduce(set.intersection, [set(item) for item in preFamilies]))
                pickS3List.append((len(interSection), subset))

            S3 = min(pickS3List)[1] # Picking the S3 which has the least interSection
            nS3 = len(S3) # stores len of S3


            while (len(L) == 3):
                try:
                    L.remove(S3) # Removes S3 and then runs the algorithm!
                except:
                    """ SPECIAL CASE - BRUTE FORCED THE SOLUTION """
                    del L[-1]
                    sub1, sub2 = printTheNumbers(L)
                    return sub1, sub2

                # Splits the S3 ==> (S31, S32)
                while (len(S3) > math.ceil(nS3/2)):
                    S31, S32 = checkS3LCP(S3, pastS3LCP)

                    if len(S31) >= len(S32):
                        L.append(S32)
                        S3 = S31
                    else:
                        L.append(S31)
                        S3 = S32

                ## Assigns bigger list to S1 and vice versa!
                if (len(L[0]) >= len(L[1])):
                    S1 = L[0]
                    S2 = L[1]
                else:
                    S1 = L[1]
                    S2 = L[0]

                ## Assigns smaller list to S31 and vice versa!
                # Combines S31 with S1/S2 and S32 with S2/S1 based on the algorithm!
                if (len(S31) <= len(S32)):
                    pass
                else:
                    temp = S31[:]
                    S31 = S32[:]
                    S32 = temp[:]

                if (len(S1) + len(S31)) <= math.ceil(n/2):
                    S1 += S31
                    if (len(S2) + len(S32)) <= math.ceil(n/2):
                        S2 += S32
                    else:
                        S3 = S32[:]
                        L.append(S3)
                else:
                    S2 += S31
                    S3 = S32[:]
                    L.append(S3)

            sub1, sub2 = printTheNumbers(L)
            return (sub1, sub2) # returns result to SuperMain

    res1, res2 = main(S, pastLCP, pastS3LCP)
    return res1, res2 # Returns results to the function call superMain(S, Number_of_Bits)


import sys
import hashlib
sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/MinPrefixCode/')
import minPrefixGen as mp # file that generates the minPrefix

def getTrapDoor():
    # sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/BloomFilter/')
    # import bloomfilter as bf # file that will generate the bloom filter!

    # SHA-1 Hash function!
    def hashIt(s):
        s = str.encode(s)
        return hashlib.sha1(s).hexdigest()

    # Extract the keys from the treeGen function
    randK = getPrivateKeys()


    randK = randK[:1]


    theRange = [4,7]
    minPrefixSet = mp.main(theRange)
    # print("min prefix of 1 - 7 is:")
    minPrefixSet = list(set(minPrefixSet))
    print(minPrefixSet)
    trap = []
    tempTrap = []
    for prefix in minPrefixSet:
        l = []
        ll = []

        for k in randK:
            element = k + prefix
            l.append(hashIt(element))
            ll.append(element)
        trap.append(l) # Contains the hashed values!
        tempTrap.append(ll) # Appends the normal element an primarily used to display

    return trap


""" PROGRAM EXECUTION BEGINS """
# Importing the bloomFilter file!
import sys
import random as rand
from binarytree import * # this will import the binary tree file

sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/BloomFilter/')
import bloomfilter as bf # file that will generate the bloom filter!

sys.path.insert(0, 'C:/Users/Stark/Desktop/Programming/Coursework/Secure-Data-Analysis/Final Project/SearchTree/')
import searchElement as search







randK = []
for i in range(7):
    randK.append(str(rand.randint(1, 1000)))

def getPrivateKeys():
    return randK



# Data

# SNum = [1,6,7,9,25,11,12,13,16,20]
SNum = [4,8]
Bits = 4

mytree = tree()
root = Node(SNum)
data = SNum
start = root
parent = root

# This function will recursively build the tree using SuperMain
def recBuildTree(x, data, parent):
    if len(x.value) == 1:
        return parent
    else:
        left, right = superMain(data, Bits)
        x.left = Node(left)
        x.right = Node(right)
        parent = x
        recBuildTree(x.left, left, parent), recBuildTree(x.right, right, parent)

# Preorder Traversal through the tree to create the bloomFilters for each node!
def preorder(tree):
    if tree:
        bloom, vr = bf.getBloomFilter(tree.value, Bits, randK) # Retrieves the bloom filter for the node data
        tree.value = (bloom, vr)
        preorder(tree.left)
        preorder(tree.right)

trap = getTrapDoor()


def searchIT(tree):
    if tree:
        # print(tree.value)
        bloomAndVR = tree.value # Gets the bloom filter and VR from the tree
        # print(bloomAndVR)
        x = search.searchForME(bloomAndVR[0], bloomAndVR[1], trap)
        if x == "FAIL":
            return
        searchIT(tree.left)
        searchIT(tree.right)

# Generating the tree
def getTree():
    # print("Data")
    print(SNum)
    print()
    # print("The Generated Tree for above data set!")
    recBuildTree(root, data, parent) # Recursively builds the tree!
    pprint(start) # Prints the tree
    preorder(start)
    searchIT(start)

    # pprint(start)
# print("Printing Trapdoor in main")

# This function call will create the tree normally and then traverse through it in Preorder
# fashion and replace the nodes with the bloom filters!
getTree() # <========= Starts the exectution
