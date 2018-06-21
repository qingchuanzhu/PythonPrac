def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    modified = False

    # nums[:head-1] guaranteed to be non-decreasing
    #head = 1

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if not modified:
                modified = True
                if i - 1 == 0 or nums[i-2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
            else:
                return False

    """
    while head < len(nums):
        if nums[head] < nums[head - 1]:
            if not modified:
                modified = True
                # check if nums[head - 1] can be decreased
                if head - 1 == 0 or nums[head-2] <= nums[head]:
                    nums[head - 1] = nums[head]
                else:
                    # no choice increase nums[head]
                    nums[head] = nums[head - 1]
                head += 1
            else:
                return False
        else:
            head += 1
            """

    print(nums)
    return True

print(checkPossibility([4,2,3,5]))
