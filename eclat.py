'''
function creates a list of items and their corresponding TIDs that they appear
input: path - path of txt file representing transaction database
output: C - a 3D list contains list of 1-size itemsets and list of the corresponding TIDs
'''
def readFile(path):
    with open(path, 'r') as f:
        listOfTIDs = [line.strip().split(' ') for line in f]
    listOfItems = sorted({item for tid in listOfTIDs for item in tid})

    C = [[[], []] for i in range(len(listOfItems))]
    for x in range(len(listOfItems)):
        C[x][0] = list(listOfItems[x])
        C[x][1] = [y+1 for y in range(len(listOfTIDs))
                   if set(listOfItems[x]).issubset(set(listOfTIDs[y]))]
    return C


'''
function removes less-support-frequent itemsets from C
input: C - a 3D list of itemsets, minsup - an integer number
output: L - 3D list of frequent itemsets
'''
def frequentItemSets(C, minsup):
    L = []
    for row in range(len(C)):
        if len(C[row][1]) >= minsup:
            L.append(C[row])
    return L
'''
Input size: size of list
worst case: average case
basic operation: if len(C[row][1]) >= minsup
count: C(n) 
=>C(n) ∈ θ(n)
'''



'''
function candidates increasing-in-1-size itemsets from L
input: L - 3D list of frequent itemsets
output: C - 3D list of itemsets
'''
def candidateItemSets(L):
    C = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            row = [[], []]
            if L[i][0][:-1] == L[j][0][:-1]:
                row[0] = sorted(set(L[i][0]).union(set(L[j][0])))
                row[1] = sorted(set(L[i][1]).intersection(set(L[j][1])))
            C.append(row)
    return C
'''
Input size:size of list
worst case:average case
basic operation: if L[i][0][:-1] == L[j][0][:-1]
count: C(n^2)
=>C(n) ∈ θ(n^2)
'''



'''
The Eclat algorithm
input: path - a path of a txt file, minsup - an integer number
output: res - list of frequent itemsets
'''
def eclat(path, minsup):
    C = readFile(path)
    L = frequentItemSets(C, minsup)  # 1-size frequent itemsets
    res = []  # the result list
    while (L):
        # add frequent itemsets (without their TIDs list) to res
        for i in range(len(L)):
            res.append(L[i][0])

        C = candidateItemSets(L)  # candidate k+1-size itemsets
        L = frequentItemSets(C, minsup)  # remove infrequent itemsets
    return res
'''
Input size: size of database
worst case: average case
basic operation: while (L)
count: C(n)
=>C(n) ∈ θ(n)
'''

if __name__ == "__main__":
    foo = eclat('input.txt', 2)
    for i in range(len(foo)):
        print('%d-size frequent itemsets:' % len(foo[i]), foo[i])
