def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    result = []
    if len(a) > len(b):
        limit = len(a) - len(b)
        b = '0'*(len(a) - len(b)) + b
        l_long = list(a)
        l_short = list(b)
    else:
        limit = len(b) - len(a)
        a = '0'*(len(b) - len(a)) + a
        l_long = list(b)
        l_short = list(a)

    carry_in = 0
    for i in list(range(len(l_short)))[::-1]:
        if i < limit and carry_in == 0:
            result = l_long[:i+1] + result
            break
        else:
            tempSum = int(l_long[i]) + int(l_short[i]) + carry_in
            carry_in = tempSum // 2
            result = [str(tempSum % 2)] + result
    if carry_in == 1:
        result = ['1'] + result

    return ''.join(result)


print(addBinary('11', '101'))
