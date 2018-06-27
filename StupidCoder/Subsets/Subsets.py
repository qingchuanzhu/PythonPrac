import math

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerSet = list()

        for i in range(2 ** (len(nums))):
            result = list()
            while i > 0:
                LSB = i & ~(i-1)
                index = int(math.log(LSB, 2))
                result.append(nums[index])
                i -= LSB
            powerSet.append(result)
        return powerSet


s = Solution()
print(s.subsets([1, 2, 3]))
