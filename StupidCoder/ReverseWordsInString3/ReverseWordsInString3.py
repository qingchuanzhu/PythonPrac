def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    return " ".join([x[::-1] for x in s.split()])


print(reverseWords(""))
