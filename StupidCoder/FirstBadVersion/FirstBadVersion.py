# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    high = n
    badv = -1
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid - 1
            badv = mid
        else:
            low = mid + 1
    return badv


def isBadVersion(version):
    if version > 5:
        return True
    else:
        return False


print(firstBadVersion(10))
