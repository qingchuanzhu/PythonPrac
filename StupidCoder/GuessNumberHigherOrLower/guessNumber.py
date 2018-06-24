class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            gue = self.guess(mid)
            if gue == 0:
                return mid
            elif gue == 1:
                high = mid - 1
            else:
                low = mid + 1


    def guess(self, num):
        if num == 6:
            return 0
        elif num > 6:
            return 1
        else:
            return -1


s = Solution()
print(s.guessNumber(10))
