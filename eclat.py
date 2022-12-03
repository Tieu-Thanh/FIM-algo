'''
function creates a list of items and their corresponding TIDs that they appear
input: path - path of txt file representing transaction database
output: C - a 3D list contains list of 1-size itemsets and list of the corresponding TIDs
'''
def readFile(path):
    # listOfTIDs = []
    # listOfItems = []
    # with open(path, 'r') as f:
    #     for line in f:
    #         tid = line.strip().split(' ')
    #         listOfTIDs.append(tid)
    #         for item in tid:
    #             if item not in listOfItems:
    #                 listOfItems.append(item)

    # C = [[list() for i in range(2)] for i in range(len(sorted(listOfItems)))]
    # for x in range(len(listOfItems)):
    #     C[x][0] = list(listOfItems[x])
    #     tids = []
    #     for y in range(len(listOfTIDs)):
    #         if set(listOfItems[x]).issubset(set(listOfTIDs[y])):
    #             tids.append(y+1)
    #     C[x][1] = tids

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


if __name__ == "__main__":
    foo = eclat('input.txt', 2)
    for i in range(len(foo)):
        print('%d-size frequent itemsets:' % len(foo[i]), foo[i])
