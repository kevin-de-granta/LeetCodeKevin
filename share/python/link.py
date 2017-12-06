
#
# DONE: put this shared definition in folder $LeetCode/share/python
#


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self, aList):
        # consider when aList is None or empty
        self.listHead = None
        cursor = None
        for elem in aList:
            node = ListNode(elem)
            if cursor is None:
                cursor = node
                self.listHead = cursor # initialize the head
            else:
                cursor.next = node
                cursor = cursor.next

    def clear(self):
        self.listHead = None

    def head(self):
        return self.listHead

    def tail(self):
        # TODO: consider situation when self.listHead is None
        cursor = self.listHead
        while True:
            if cursor.next is None:
                return cursor
            else:
                cursor = cursor.next

    # TODO: for all append* functions, consider the situation when self.listHead is None.

    def append(self,val):
        return self.appendVal(val)

    def appendVal(self, val):
        """
        To append a value to the end of the list, that is, behind the tail.
        """
        newNode = ListNode(val)
        tail = self.tail()
        tail.next = newNode
        return self

    def appendNode(self, node):
        tail = self.tail()
        tail.next = node
        return self

    def appendList(self, lst):
        newHead = lst.listHead
        tail = self.tail()
        tail.next = newHead
        return self

    # TODO: a bug is, if an instance of LinkedList is appended to itself, it would result in a circular linked list, and displaying a circular list would cause a dead loop.
    # TODO: debug this function.
    def append2(self, val):
        if isinstance(self, ListNode):
            tail = self.tail()
            tail.next = val
            return self # wrong: return self.header()
        if isinstance(val, LinkedList):
            tail = self.tail()
            tail.next = val.head()
            return self
        else:
            node = ListNode(val)
            return self.append(node)

    def reverse(self):
        pass

    def isCircle(self):
        pass

    def display(self):
        cursor = self.listHead
        buff = ''
        if cursor is None:
            return
        buff = buff + str(cursor.val)
        while True:
            cursor = cursor.next
            if cursor is None:
                break
            buff = buff + ' -> ' + str(cursor.val)
        print buff



