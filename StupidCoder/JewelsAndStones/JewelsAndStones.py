
def numJewelsInStones(J, S):
    """
    :type J: str characters in J are distinct
    :type S: str
    :rtype: int
    """

    numberOfJ = 0
    D = {}
    for stone in S:
        if stone in D:
            D[stone] += 1
        else:
            D[stone] = 1

    for j in J:
        if j in D:
            numberOfJ += D[j]
    return numberOfJ


print(numJewelsInStones('aA','aAAbbbbb'))