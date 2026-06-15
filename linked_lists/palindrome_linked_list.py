# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        straight_list = []
        curr = head
        while curr:
            straight_list.append(curr.val)
            curr = curr.next
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        reversed_list = []
        while prev:
            reversed_list.append(prev.val)
            prev= prev.next
        return straight_list == reversed_list
            