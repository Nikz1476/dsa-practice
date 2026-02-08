# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #time, space (extra array) - O(n)
        # nodes = []
        # current = head

        # while current:
        #     nodes.append(current)
        #     current = current.next

        # return nodes[len(nodes) // 2]


        # #Better - 2 passes
        # #time - O(N)
        # #space - O(1)
        # count = 0
        # current = head

        # # First pass: count nodes
        # while current:
        #     count += 1
        #     current = current.next

        # # Second pass: move to middle
        # current = head
        # for _ in range(count // 2):
        #     current = current.next

        # return current


        #optimal - slow,fast pointer
        #complexity same as above
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow