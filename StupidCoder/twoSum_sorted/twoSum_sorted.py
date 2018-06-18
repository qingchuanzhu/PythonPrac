import time


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start_time = time.time()
    i = 0
    while i < len(numbers):
        partner = target - numbers[i]
        try:
            thing_index = numbers[i + 1:].index(partner)
            print("--- %s seconds ---", time.time() - start_time)
            return [i + 1, thing_index + i + 2]
        except ValueError:
            low = i
            high = len(numbers) - 1
            index = low
            num = numbers[i]
            while low <= high:
                mid = low + (high - low) // 2
                if numbers[mid] < num:
                    low = mid + 1
                elif numbers[mid] > num:
                    high = mid - 1
                else:
                    low = mid + 1
                    index = mid
            i = index + 1
            continue


print(twoSum([2, 5, 11, 15], 7))
