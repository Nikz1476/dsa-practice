# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = head
        # count = 0 

        # while slow:
        #     count += 1
        #     slow = slow.next

        # slow = head
        # for _ in range ((count //2)-1):
        #     slow = slow.next

        # slow.next = slow.next.next
        
        # return head

        #both methods same complexity
        #time - O(n), space - O(1)
        #optimal - two pointers
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # delete middle node
        prev.next = slow.next

        return head