from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def printListNode(self, head: Optional[ListNode]):
        node = head
        while node:
            print(node.val, end=' ')
            node = node.next
        print()


l8 = ListNode(8, None)
l7 = ListNode(7, l8)
l6 = ListNode(6, l7)
l5 = ListNode(5, l6)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)


a = Solution()
a.printListNode(l1)
a.printListNode(a.reverseList(l1))
a.printListNode(a.reverseList(None))
a.printListNode(a.reverseList(l8))
