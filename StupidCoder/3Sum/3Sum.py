import time


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    start_time = time.time()
    result = []
    nums.sort()
    if nums[0] > 0 or nums[-1] < 0:
        return result
    index_0_first = find_firstOf(nums, 0)
    index_0_last = find_lastOf(nums, 0)
    # handle three 0 case
    if index_0_last - index_0_first >= 2:
        result.append([0, 0, 0])
    # [index_0_last + 1, len(nums)] positive numbers
    # [0, index_0_first -1] negative numbers

    if index_0_first == 0 or index_0_last == (len(nums) - 1):
        return result
    # case 1: Have 0 in nums, 1 pos, 1 negative
    if index_0_first != -1 and index_0_last != -1:
        index = 0
        while index <= index_0_first - 1:
            neg = nums[index]
            if -neg in nums[index_0_last + 1:]:
                result.append([neg, 0, -neg])
            index = find_lastOf(nums[index:index_0_first], neg) + 1 + index

    if index_0_first == index_0_last == -1:
        index_0_last = find_startOfPositive(nums) - 1
        index_0_first = index_0_last + 1

    last_index = len(nums) - 1

    # case 2: 2 pos 1 neg [neg, pos1, pos2] where pos1<=pos2
    neg_set = list(set(nums[:index_0_first]))
    for neg in neg_set:
        target = -neg
        index = index_0_last + 1
        pos1 = nums[index]
        while pos1 <= target - pos1:
            if target - pos1 in nums[index + 1:]:
                result.append([neg, pos1, target - pos1])
            index = find_lastOf(nums[index:], pos1) + 1 + index
            if index <= last_index:
                pos1 = nums[index]
            else:
                break

    # case 3: 2 neg 1 pos [neg1, neg2, pos] where neg1<=neg2
    pos_set = list(set(nums[index_0_last + 1:]))
    for pos in pos_set:
        target = -pos
        index = 0
        neg1 = nums[index]
        while neg1 <= target - neg1:
            if target - neg1 in nums[index+1:index_0_first]:
                result.append([neg1, target - neg1, pos])
            index = find_lastOf(nums[index:index_0_first], neg1) + 1 + index
            if index <= last_index:
                neg1 = nums[index]
            else:
                break

    print("--- %s seconds ---", time.time() - start_time)
    return result


def find_firstOf(nums, target):
    low = 0
    high = len(nums) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            index = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return index


def find_lastOf(nums, target):
    low = 0
    high = len(nums) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            index = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return index


def find_startOfPositive(nums):
    low = 0
    high = len(nums) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < 0:
            low = mid + 1
        else:
            index = mid
            high = mid - 1

    return index


print(threeSum([-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, -1, -4]))
