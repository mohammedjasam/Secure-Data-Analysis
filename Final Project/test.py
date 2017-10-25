# Enter the range for the prefix set
r = list(map(int, input("Enter the range space separated!\n").split()))
d = {}
l = []
### ___________________________________________________________________________###
for x in range(r[0], r[-1]+1):
    if x == 0:
        d[1] = [x]
    elif x.bit_length() in d.keys():
        d[x.bit_length()].append(x)
    else:
        d[x.bit_length()] = [x]
print(d)
