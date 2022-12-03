'''
functions reads txt file to retrieve data
input: input - path of txt file representing transaction database
output: listOfTIDs - a list of transactions; listOfItems - list of distinct items
'''
def readTransDB(input):
    with open(input, 'r') as f:
        listOfTIDs = [[list(item)
                       for item in line.strip().split(' ')] for line in f]

    listOfItems = []
    for tid in listOfTIDs:
        for item in tid:
            if item not in listOfItems:
                listOfItems.append(item)

    return listOfTIDs, listOfItems
'''
input size: number lines of file
worst case: average case 
basic operation: if item not in listOfItems 
count: C(n) 
=>C(n) ∈ θ(n)
'''



'''
function removes less-support-frequent itemsets from C
input: C - list of itemsets; passC - list of combinations; minsup - an integer number
output: L - list of frequent itemsets
'''
def getFrequentItemSets(C, passC, minsup):
    L = []
    for itemSet in C:
        count = 0
        for tid in passC:
            if itemSet in tid:
                count += 1
        if count >= minsup:
            L.append(itemSet)
    return L
'''
input size: size list of itemsets
worst case: average case
basic operation: if itemSet in tid
count: C(n^2)
=> C(n) ∈ big θ(n^2)
'''



'''
function candidates list of itemsets from L
input: L - list of frequent itemsets
output: C - list of increase-in-size-1 itemsets
'''
def candidateItemSets(L):
    C = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i][:-1] == L[j][:-1]:
                C.append(sorted(set(L[i]).union(set(L[j]))))
    return C
'''
input size: size of list
worst case: average case
basic operation: if L[i][:-1] == L[j][:-1]
count: C(n^2) 
=>C(n) ∈ θ(n^2)
'''



'''
function creates the candidate itemsets for passing
input: prevPassC - the previous passed itemsets, C - the candidate itemsets
output: passC - the candidate itemsets for passing
'''
def getPassC(prevPassC, C):
    passC = []
    if (C):
        k = len(C[0]) - 1  # last index
    for t in range(len(prevPassC)):
        Ct = []
        for c in C:
            a = c[:-1]
            b = c[:k-1] + c[k:]
            if a in prevPassC[t] and b in prevPassC[t]:
                Ct.append(c)
        if Ct:
            passC.append(Ct)
    return passC
'''
Input size: size of list
worst case: average case
basic operation: if a in prevPassC[t] and b in prevPassC[t]
count: C(n^2)
=> C(n) ∈ θ(n^2)
'''



'''
The aprioriTID
input: path - txt file, minsup - int
output: res - list of frequent itemsets
'''
def aprioriTID(path, minsup):
    C_, C = readTransDB(path)
    L = getFrequentItemSets(C, C_, minsup)
    res = []
    while (L):
        res.append(L)
        C = candidateItemSets(L)
        C_ = getPassC(C_, C)
        L = getFrequentItemSets(C, C_, minsup)
    return res
'''
Input size: size of database
worst case: average case
basic operison: while (L)
count: C(n)
=> C(n) ∈ θ(n)
'''

if __name__ == "__main__":
    foo = aprioriTID('input.txt', 2)
    for i in foo:
        print('%d-size frequent itemsets:' % (len(i[0])), i)
