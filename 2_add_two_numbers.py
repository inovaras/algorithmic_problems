from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sumNodes(self, n1, n2, in_mind):
        if n1.val + n2.val + in_mind < 10:
            node = ListNode(n1.val + n2.val + in_mind)
            in_mind = 0
        else:
            node = ListNode((n1.val + n2.val + in_mind) % 10)
            in_mind = (n1.val + n2.val + in_mind) // 10
        return node, in_mind

    def sumNode(self, node, n1, in_mind):
        if n1.val + in_mind < 10:
            node = ListNode(n1.val + in_mind)
            in_mind = 0
        else:
            node = ListNode((n1.val + in_mind) % 10)
            in_mind = (n1.val + in_mind) // 10

        return node, in_mind

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node, in_mind = self.sumNodes(l1, l2, in_mind=0)
        l1 = l1.next
        l2 = l2.next
        head = node
        while l1 and l2:
            node.next, in_mind = self.sumNodes(l1, l2, in_mind)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        else:
            while l1:
                node.next, in_mind = self.sumNode(node, l1, in_mind)
                node = node.next
                l1 = l1.next
            while l2:
                node.next, in_mind = self.sumNode(node, l2, in_mind)
                node = node.next
                l2 = l2.next
        if in_mind != 0:
            node.next = ListNode(in_mind)

        return head

    def print_list_node(self, l: Optional[ListNode]):
        while l:
            print(l.val, end=' ')
            l = l.next
        print()


n3 = ListNode(9, None)
n2 = ListNode(8, n3)
n1 = ListNode(7, n2)

l3 = ListNode(9, None)
l2 = ListNode(8, l3)
l1 = ListNode(7, l2)

a = Solution()
a.print_list_node(n1)
a.print_list_node(l1)
a.print_list_node(a.addTwoNumbers(n1, l1))

a.print_list_node(n1)
a.print_list_node(l2)
a.print_list_node(a.addTwoNumbers(n1, l2))

a.print_list_node(n1)
a.print_list_node(l3)
a.print_list_node(a.addTwoNumbers(n1, l3))
