# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos1 = head
        pos2 = head
        count = 1
        
        while(pos1.next != None):
            count+= 1
            pos1 = pos1.next
        print(count)
        if count==1:
            return None
        elif count==2:
            pos2.next = None
            return head
        else:
            mid = count//2
            end = 0
            while(end < (mid-1)):
                end += 1
                pos2 = pos2.next
            pos2.next = pos2.next.next
        return head
        