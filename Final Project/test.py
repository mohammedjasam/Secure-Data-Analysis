# # Enter the range for the prefix set
# r = list(map(int, input("Enter the range space separated!\n").split()))
# d = {}
# l = []
# ### ___________________________________________________________________________###
# for x in range(r[0], r[-1]+1):
#     if x == 0:
#         d[1] = [x]
#     elif x.bit_length() in d.keys():
#         d[x.bit_length()].append(x)
#     else:
#         d[x.bit_length()] = [x]
# print(d)


finList = []
daffuqList = []

def joinList(l):
    return "".join(l)

def checkStars(pivot, l):
    cPivot = 0
    cL = 0
    pivot, l = list(pivot), list(l)
    for x in pivot:
        if x == "*":
            cPivot += 1
    for x in l:
        if x == "*":
            cL += 1

    if cPivot >= cL:
        return joinList(pivot)
    else:
        return joinList(l)



def assignPivot(l):
    pivot = l[0]
    for x in range(1,len(l)):
        pivot = checkStars(pivot, l[x])
    return pivot



def compare(pivot, l):
    pivot = list(pivot)
    l = list(l)

    for x in range(5):
        if not(pivot[x] == l[x] or pivot[x] == "*" or l[x] == "*"):
            return 0
    return 1




def start(l):
    pivot = assignPivot(l)
    for index in range(len(l)):
        res = compare(pivot, l[index])

        if res == 0:
            pivot = checkStars(pivot, l[index])
            if not(l[index] in finList):
                finList.append(l[index])
    # print(pivot)
    if not(pivot in finList):
        finList.append(pivot)
    # start()

def main(l):
    start(l)
    daffuqList.append(finList[-1])
    i = 0
    while(len(finList)>0):
        del finList[-1]
        l = finList[:]
        print(l, finList)
        start(l)
        daffuqList.append(finList[-1])
        i +=1
        print(daffuqList)



l = ['0001*', '001**', '0010*', '0011*', '01***', '010**', '0100*', '0101*', '011**', '0110*', '0111*']
main(l)
