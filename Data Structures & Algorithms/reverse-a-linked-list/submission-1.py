# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, new = head, []

        while curr:
            new.append(curr.val)
            curr = curr.next

        new.reverse()

        curr, i = head, 0
        while curr:
            curr.val = new[i]
            i += 1
            curr = curr.next
        return head



