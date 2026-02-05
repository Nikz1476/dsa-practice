# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force - time and space O(n)
        # values = []
        # curr = head

        # while curr:
        #     values.append(curr.val)
        #     curr = curr.next

        # dummy = ListNode(0)
        # curr = dummy

        # for val in reversed(values):
        #     curr.next = ListNode(val)
        #     curr = curr.next

        # return dummy.next

        # Optimal - inplace 
        # time - O(n)
        # space - O(1)
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # store next
            curr.next = prev        # reverse pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev