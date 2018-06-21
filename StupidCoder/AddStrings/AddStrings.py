def addStrings(num1, num2):
    """
    :type num1: str >=0
    :type num2: str >= 0
    :rtype: str
    """
    if num1 == '0':
        return num2
    if num2 == '0':
        return num1

    L_long = []
    L_short = []
    Sum = []
    if len(num1) > len(num2):
        L_long = list(num1)
        L_short = list(num2)
    else:
        L_long = list(num2)
        L_short = list(num1)

    carry_in = '0'
    for i in range(-1, -(len(L_short)+1), -1):
        result_tuple = addDigits(L_short[i], L_long[i], carry_in)
        carry_in = result_tuple[1]
        Sum = [result_tuple[0]] + Sum

    end_index = len(L_long) - len(L_short) - 1
    if carry_in == '1':
        for i in range(end_index, -1, -1):
            if L_long[i] == '9':
                Sum = ['0'] + Sum
                end_index = i - 1
            else:
                tuple = addDigits(L_long[i], '0', carry_in)
                Sum = [tuple[0]] + Sum
                carry_in = '0'
                end_index = i - 1
                break

    # append rest of long to the beginning
    if carry_in == '1':
        Sum = ['1'] + Sum
    else:
        Sum = L_long[:end_index+1] + Sum
    return ''.join(Sum)


def addDigits(char1, char2, carry):
    """
        :type char1: str single digit
        :type char2: str single digit
        :rtype: (result, carryout)
    """

    add1 = int(char1)
    add2 = int(char2)
    carryIn = int(carry)
    sumtwo = add1 + add2 + carryIn
    if sumtwo >= 10:
        return str(sumtwo - 10), '1'
    else:
        return str(sumtwo), '0'


print(addStrings('123', '456'))
