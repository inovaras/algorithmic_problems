from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def is_first_less_second(self, n1, n2):
        if n1 is None:
            return False
        return n1.val < n2.val
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = lists
        temp = None
        answer = None
        while True:
            min_node = None
            a = None
            for i, head in enumerate(heads):
                if head is not None:
                    if not self.is_first_less_second(min_node, head):
                        min_node = head
                        a = i
            if min_node is None:
                return answer
            if answer is None:
                answer = min_node
            else:
                temp.next = min_node
            temp = min_node
            heads[a] = heads[a].next

