# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        prev_node = None
        current_node = head
        
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        return prev_node

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        reversed_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        
        return reversed_head
