# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #brute force - time O(n), space O(1)
        ## Step 1: get length
        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next

        # # Step 2: remove (length - n)th node
        # if length == n:
        #     return head.next  # removing the head

        # curr = head
        # for _ in range(length - n - 1):
        #     curr = curr.next

        # curr.next = curr.next.next
        # return head

        
        #better using stack but extra memory 
        #time, space - O(n)
        # stack = []
        # curr = head

        # while curr:
        #     stack.append(curr)
        #     curr = curr.next

        # # remove head
        # if n == len(stack):
        #     return head.next

        # prev = stack[-n - 1]
        # prev.next = prev.next.next
        # return head
        
        
        
        #optimal two pointers 
        # time - O(n), space - O(1)
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next

        # remove nth node
        slow.next = slow.next.next

        return dummy.next
