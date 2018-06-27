import ListNode

class listParser:
    def createListNodes(self, sortedLists):
        result = []
        for l in sortedLists:
            dummyHead = ListNode.ListNode(None)
            current = dummyHead
            for i in range(len(l)):
                node = ListNode.ListNode(l[i])
                current.next = node
                current = node

            result.append(dummyHead.next)
        return result