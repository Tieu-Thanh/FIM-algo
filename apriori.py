'''
functions reads txt file to retrieve data
input: input - path of txt file representing transaction database
output: listOfTIDs - a list of transactions; listOfItems - list of distinct items
'''
def readTransDB(input):
    with open(input, 'r') as f:
        listOfTIDs = [line.strip().split(' ') for line in f]

    listOfItems = sorted({item for tid in listOfTIDs for item in tid})

    return listOfTIDs, listOfItems
'''
input size: number lines of file
worst case: average case 
basic operation: addition in line 10
count: C(n) 
=>C(n) belong to big theta(n)
'''


'''
function removes less-support-frequent itemsets from C
input: C - list of itemsets; transDB - list of transactions; minsup - an integer number
output: L - list of frequent itemsets
'''
def getFrequentItemSets(C, transDB, minsup):
    L = []
    for itemSet in C:
        count = 0
        for tid in transDB:
            if set(itemSet).issubset(set(tid)):
                count += 1
        if count >= minsup:
            L.append(itemSet)
    return L
'''
input size: size list of itemsets
worst case: average case
basic operation: if set(itemSet).issubset(set(tid))
count: C(n^2)
=> C(n) belong to big theta(n^2)
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
=>C(n) belong to big theta(n^2)
'''


'''
The Apriori algorithm
input: path - txt file, minsup - integer number
output: res - list of frequent itemsets
'''
def apriori(path, minsup):
    dbs, C = readTransDB(path) # C is the 1-size item set
    L = getFrequentItemSets(C, dbs, minsup) # the frequent 1-size item set
            
    res = [] # result
    while(L):
        res.append(L) # store the previous frequent itemsets L
        C = candidateItemSets(L) # join step
        L = getFrequentItemSets(C, dbs, minsup) # prune step

    return res
'''
input size: size of database
worst case: average case
basic operation: while(L)
count: C(n) 
=>C(n) belong to big-theta(n)
'''


if __name__ == "__main__":
    print(apriori('input.txt', 2))


