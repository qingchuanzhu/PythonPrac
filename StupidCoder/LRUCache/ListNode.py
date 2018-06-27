class ListNode:

    val = None
    key = None
    nextNode = None
    prevNode = None

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.nextNode = None
        self.prevNode = None