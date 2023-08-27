class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def initialCheck(self,node_a,node_b) :
        if node_a is None :
            return node_b,True
        if node_b is None :
            return node_a,True
        return None,False

    def makeLinkedList(self,node,cur,new_head) :
        if new_head is None :
            new_head = ListNode(node.val)
            cur = new_head
        else :
            cur.next = ListNode(node.val)
            cur = cur.next
        return new_head,cur

    def completeLinkedList(self,node,cur,new_head) :
        while node :
            new_head,cur = self.makeLinkedList(node,cur,new_head)
            node = node.next
        return cur,new_head
        
    def mergeTwoLists(self, list1: [ListNode], list2:[ListNode]) ->[ListNode]:
        
        new_head,cur,node_a,node_b = None,None,list1,list2
        nn,check = self.initialCheck(node_a,node_b)
        if check : 
            return nn 
        cur = None
        while node_a and node_b :
            if node_a.val > node_b.val :
                new_head,cur = self.makeLinkedList(node_b,cur,new_head)
                node_b = node_b.next
            else :
                new_head,cur = self.makeLinkedList(node_a,cur,new_head)
                node_a = node_a.next
        
        cur,new_head = self.completeLinkedList(node_a,cur,new_head)
        cur,new_head = self.completeLinkedList(node_b,cur,new_head)

        
        return new_head
