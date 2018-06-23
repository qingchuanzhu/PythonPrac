import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        base = int(math.sqrt(area))
        while base >= 1:
            if area % base == 0:
                return int(area / base), base
            base -= 1


s = Solution()
print(s.constructRectangle(56))
