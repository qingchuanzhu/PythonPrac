class NumArray:
    V = list() # BIT
    num = list() #original list

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.V = [0] * (len(nums) + 1)
        self.num = nums
        for i in range(len(nums)):
            additive = self.num[i]
            i += 1
            while i < len(self.V):
                self.V[i] += additive
                i = i + (i & -i)

    def update(self, i, val):
        """
        :type i: int zero-based
        :type val: int
        :rtype: void
        """
        additive = val - self.num[i]
        self.num[i] = val
        i += 1
        while i < len(self.V):
            self.V[i] += additive
            i = i + (i & -i)


    def sumRange(self, i, j):
        """
        :type i: int zero-based
        :type j: int zero-based
        :rtype: int
        """
        j += 1
        firstSum = self.V[0]
        secondSum = self.V[0]
        while i > 0:
            firstSum += self.V[i]
            i = i - (i & -i)

        while j > 0:
            secondSum += self.V[j]
            j = j - (j & -j)

        return secondSum - firstSum


numArray = NumArray([7, 2, 7, 2, 0])
print(numArray.V)
numArray.update(0, 2)
print(numArray.V)
numArray.update(0, 9)
print(numArray.V)
print(numArray.sumRange(0, 0))

