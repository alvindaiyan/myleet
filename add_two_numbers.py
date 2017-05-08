# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)
        c = 1 if (l1.val + l2.val + carry) >= 10 else 0
        val = (l1.val + l2.val + carry) % 10
        if l1.next or l2.next or c > 0:
            node = ListNode(val)
            node.next = self.addTwoNumbers(l1.next, l2.next, c)
            return node
        else:
            return ListNode(val)