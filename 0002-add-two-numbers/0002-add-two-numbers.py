# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        count = 1
        num1, num2 = 0, 0
        out = 0
        while p1:
            num1 += (p1.val)*(count)
            count = count*10
            p1 = p1.next
        count = 1
        while p2:
            num2 += (p2.val)*(count)
            count = count*10
            p2 = p2.next
        out = num1 + num2
        out = str(out)[::-1]
        head = ListNode(val = out[0])
        curr = head
        for i in range(1, len(out)):
            curr.next = ListNode(out[i])
            curr = curr.next
        return head
            
