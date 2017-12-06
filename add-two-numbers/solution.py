# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from link import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        [n1, n2] = [l1, l2]
        [sumVal, carry] = [0, 0]
        [res, tail] = [None, None]
        while True:
            [sumVal, carry] = [n1.x + n2.x + carry, 0]
            if sumval >= 10:
                [sumVal, carry] = [sumval - 10, 1]
            if tail is None:
                tail = ListNode(sumVal)
            else:
                tail.next = ListNode(someVal)

