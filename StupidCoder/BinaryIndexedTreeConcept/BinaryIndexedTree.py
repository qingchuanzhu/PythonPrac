class FenwickTree:
    V = list()

    def update(self, i, num):
        """
        :type i: int
        :type num: int
        """

        while i < len(self.V):
            self.V[i] += num
            i = i + (i & -i)

    def prefixSum(self, i):
        """
        :type i: int
        """
        prefixsum = self.V[0]
        while i > 0:
            prefixsum += self.V[i]
            i = i - (i & -i)
        return prefixsum

    def __init__(self, list):
        self.V = [0] * (len(list) + 1)
        for i in range(1, len(self.V), 1):
            self.update(i, list[i-1])


fenwickTree = FenwickTree([2, 0, 1, 1, 1, 0, 4, 4, 0, 1, 0, 1, 2, 3, 0])
print(fenwickTree.V)
print(fenwickTree.prefixSum(15))
