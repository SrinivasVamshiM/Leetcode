# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        evenhead = even = ListNode()
        oddhead = odd = ListNode()
        pos= head
        
        if pos == None or pos.next == None:
            return head
        evencount =0
        oddcount=0
        iseven = False
        while pos:
            if iseven:
                even.next = pos
                even = even.next
            else:
                odd.next = pos
                odd = odd.next
            pos = pos.next
            iseven = not iseven
        odd.next = evenhead.next
        even.next = None
        
        return oddhead.next