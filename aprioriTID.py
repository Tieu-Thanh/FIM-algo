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


if __name__ == "__main__":
    foo = aprioriTID('input.txt', 2)
    for i in foo:
        print('%d-size frequent itemsets:' % (len(i[0])), i)
