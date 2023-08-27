class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getCarryDigit(self,ptr_a = None,ptr_b = None,carry = 0) :
        num = carry
        if ptr_a :
            num += ptr_a.val
        if ptr_b :
            num += ptr_b.val 
        carry = num//10
        digit = num % 10
        return carry,digit

    def move_forward(self,cur,ptr_a = None,ptr_b = None) :
        cur = cur.next
        if ptr_a :
            ptr_a = ptr_a.next
        if ptr_b :
            ptr_b = ptr_b.next
        return cur,ptr_a,ptr_b

    def main_body(self,ptr_a,ptr_b,cur,carry = 0) :
        carry,digit = self.getCarryDigit(ptr_a,ptr_b,carry)
        cur.next = ListNode(digit)
        cur,ptr_a,ptr_b = self.move_forward(cur,ptr_a,ptr_b)

        return ptr_a,ptr_b,carry,cur

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        cur = new_head = ListNode(0)
        ptr_a,ptr_b = l1,l2
        carry = 0
        while ptr_a and ptr_b :
            ptr_a,ptr_b,carry,cur = self.main_body(ptr_a,ptr_b,cur,carry)
        while ptr_a :
            ptr_a,ptr_b,carry,cur = self.main_body(ptr_a,ptr_b,cur,carry)
        while ptr_b :
            ptr_a,ptr_b,carry,cur = self.main_body(ptr_a,ptr_b,cur,carry)
        if carry :
            cur.next = ListNode(1)
        return new_head.next