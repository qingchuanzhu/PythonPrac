import ListNode

class LRUCache:

    capacity = 0
    dummyNode = head = tail = None
    D = {}

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.D = {}
        self.dummyNode = ListNode.ListNode(None, None)
        self.head = self.dummyNode.nextNode
        self.tail = self.dummyNode.nextNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.D:
            self.recentUsed(self.D[key])
            return self.D[key].val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.D:
            self.D[key].val = value
            self.recentUsed(self.D[key])
        else:
            if len(self.D) == self.capacity:
                self.evictLRU()
                self.put(key, value)
            else:
                node = ListNode.ListNode(key, value)
                self.D[key] = node
                self.recentUsed(node)

    def evictLRU(self):
        self.D.pop(self.head.key)
        if self.head.nextNode is None:
            self.head = None
            self.tail = None
            self.dummyNode.nextNode = None
            return
        self.head = self.head.nextNode
        self.head.prevNode = self.dummyNode
        self.dummyNode.nextNode = self.head

    def recentUsed(self, node):
        if node.nextNode is None and node.prevNode is not None:
            return
        else:
            if self.tail is not None:
                # node is in the middle
                nextNode = node.nextNode
                prevNode = node.prevNode
                self.tail.nextNode = node
                node.prevNode = self.tail
                node.nextNode = None
                self.tail = node

                if prevNode is not None and nextNode is not None:
                    prevNode.nextNode = nextNode
                    nextNode.prevNode = prevNode
                self.head = self.dummyNode.nextNode

            else:
                # first node
                self.dummyNode.nextNode = node
                node.prevNode = self.dummyNode
                self.head = node
                self.tail = node


obj = LRUCache(1)
obj.put(2, 1)
print(obj.get(2))
obj.put(3, 2)
print(obj.get(2))
print(obj.get(3))
