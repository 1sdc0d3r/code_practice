class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head):
    currentF = head
    currentS = head
    if head is not None:
        while True:
            if currentF.next == None:
                return currentS
            if currentF.next.next == None:
                return currentS.next
            currentF = currentF.next.next
            currentS = currentS.next
