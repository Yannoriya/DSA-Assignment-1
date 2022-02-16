def printknapsack(weight, pellets, val, n):
    K = [[0 for w in range(weight + 1)]
         for i in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif pellets[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - pellets[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # storing the result of Knapsack
    result = K[n][weight]
    print("The maximum value that can be obtained while using the knapsack algorithm is ", result)

    w = weight
    for i in range(n, 0, -1):
        if result <= 0:
            break
        #  the result will either come from the top (K[i-1][w]) or from (val[i-1] + K[i-1] [w-wt[i-1]]) like in the Knapsack table. If it comes from the latter one that would mean the item is included.
        if result == K[i - 1][w]:
            continue
        else:

            # This item is included.
            print("%10s       %10s" % ("Weights", "Values"))
            print("%10d       %10d" % (pellets[i - 1], val[i-1]))

            # Since this weight is included its value is deducted
            result = result - val[i - 1]
            w = w - pellets[i - 1]


matching_values = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]
matching_pellets = [5, 3, 1, 6, 8, 4, 11, 12]
W = 20
n = len(matching_values)


printknapsack(W, matching_pellets, matching_values, n)
