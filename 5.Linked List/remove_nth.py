class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        if head is None or head.next is None :
            return None
        first,second = head,head
        for i in range(n) :
            first = first.next
        if first :
            while first.next :
                first = first.next
                second = second.next
            second.next = second.next.next
        else :
            return second.next
        return head