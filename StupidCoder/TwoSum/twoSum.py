from collections import defaultdict


def two_sum(array, target):
    # build up hash
    d = defaultdict(list)
    i = 0
    for x in array:
        if x in d:
            d[x] = d[x].append(i)
        else:
            d[x] = [i]
        i = i+1

    print(d)
    
    for x in array:
        if target - x in d:
            if d[x][0] != d[target - x][0]:
                return d[x][0], d[target - x][0]
            else:
                if len(d[x]) >= 2:
                    return d[x][0], d[x][1]
    return -1, -1


print(two_sum([3, 3], 6))
