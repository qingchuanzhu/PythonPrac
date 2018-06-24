class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        D1 = {}
        D2 = {}

        for num in nums1:
            if num in D1:
                D1[num] += 1
            else:
                D1[num] = 1

        for num in nums2:
            if num in D2:
                D2[num] += 1
            else:
                D2[num] = 1

        if len(D2) < len(D1):
            temp = D1
            D1 = D2
            D2 = temp

        # now D1 is shorter than D2
        result = []
        for key in D1:
            if key in D2:
                result += [key] * (min(D1[key], D2[key]))

        return result


s = Solution()
print(s.intersect([1, 2], [1, 1]))
