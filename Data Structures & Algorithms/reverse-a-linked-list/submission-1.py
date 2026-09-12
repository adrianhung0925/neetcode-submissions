# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return

        left = head
        right = head.next
        
        head.next = None

        while right != None:
            next_node = right.next
            right.next = left
            left = right
            right = next_node
        return left
