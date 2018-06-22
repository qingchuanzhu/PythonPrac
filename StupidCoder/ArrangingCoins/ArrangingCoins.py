import math


def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    return int((math.sqrt(1 + 8 * n) - 1) // 2)


print(arrangeCoins(8))
