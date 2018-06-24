# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode sorted
        :type l2: ListNode sorted
        :rtype: ListNode
        """
        current = ListNode(None)
        head = current
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l2 is not None:
            current.next = l2
        elif l1 is not None:
            current.next = l1

        return head.next


def listParser(str):
    nodes = str.split('->')
    l_ListNode = []
    for n in nodes:
        node = ListNode(n)
        l_ListNode.append(node)
    for i in range(len(l_ListNode) - 1):
        l_ListNode[i].next = l_ListNode[i+1]
    return l_ListNode[0]


def printList(head):
    while head is not None:
        print(head.val)
        head = head.next


list1 = '5->7->9'
list2 = '1->3->4'
head1 = listParser(list1)
head2 = listParser(list2)
s = Solution()
head = s.mergeTwoLists(head1, head2)
printList(head)
