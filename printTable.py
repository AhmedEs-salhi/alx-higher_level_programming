def printTable(table):
    #maxWordLength = max(set(len(j) for i in table for j in i))
    lines = len(table)
    columns = len(table[0])
    wordLengthList = [[len(table[i][j]) for j in range(columns)] for i in range(lines)]
    maxWordLengthList = [max(i) for i in wordLengthList]

    for j in range(columns):
        for i in range(lines):
            maxWordLength = max(set(
                len(table[i][j]) for j in range(columns) for i in range(lines)))
            print("{:>{}}".format(table[i][j], maxWordLengthList[i]), end=" ")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
