# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # values = []           O(n),O(n)

        # curr = head
        # while curr:
        #     values.append(curr.val)
        #     curr = curr.next

        # curr = head
        # for val in reversed(values):
        #     curr.val = val
        #     curr = curr.next

        # return head
        
        
        
        # better using stack  - O(n),O(n)
        # if not head:
        #     return None

        # stack = []
        # curr = head

        # while curr:
        #     stack.append(curr)
        #     curr = curr.next

        # new_head = stack.pop()
        # curr = new_head

        # while stack:
        #     curr.next = stack.pop()
        #     curr = curr.next

        # curr.next = None

        # return new_head

        
        #Optimal - iterative        O(n),O(1)
        # prev = None
        # curr = head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # return prev



        #Optimal recursive - O(n),O(n)
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head