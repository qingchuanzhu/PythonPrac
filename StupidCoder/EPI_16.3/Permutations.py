def permutations(A):
    """
    prints all permutation of A
    :type A: list
    :rtype:
    """
    directedPermutations(0, A)


def directedPermutations(i, A):
    """
    prints all permutations of A[i:]
    :param i:
    :param A:
    :return:
    """
    if i == len(A) - 1:
        print(A)
        return

    for j in range(i, len(A), 1):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

        directedPermutations(i+1, A)

        temp = A[i]
        A[i] = A[j]
        A[j] = temp


permutations([2, 3, 5, 7])
