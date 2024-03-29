# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev , curr, ans = None, head, head.next

        while curr and curr.next:
            adj = curr.next
            if prev:
                prev.next = adj
            curr.next, adj.next = adj.next, curr
            prev, curr = curr, curr.next
        
        return ans or head
        