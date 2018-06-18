import time


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        Keep a variable for the index, using list.index() is costly   
        '''

        start_time = time.time()
        d = {}
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in d:
                print("--- %s seconds ---" % (time.time() - start_time))
                return [d[partner], i]
            else:
                d[nums[i]] = i


print(twoSum([2, 7, 2, 15], 9))
