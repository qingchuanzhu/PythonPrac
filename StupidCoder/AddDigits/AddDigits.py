def addDigits(num):
    """
    :type num: int
    :rtype: int
    """

    D = {}

    for i in list(range(10)):
        for j in list(range(10)):
            if i + j < 10:
                D[(i,j)] = i + j
            else:
                D[(i,j)] = (i + j) % 10 + 1

    L = [int(x) for x in list(str(num))]
    while len(L) > 1:
        if len(L) % 2 == 1:
            L = [0] + L
        # dive L into half
        newL = []
        for i in list(range(len(L)))[::2]:
            newL.append(D[(L[i], L[i+1])])
        L = newL

    return L[0]


print(addDigits(10000000000))
