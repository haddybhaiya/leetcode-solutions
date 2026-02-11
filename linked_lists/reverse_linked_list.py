class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr :
            nxt_nd = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_nd
        return prev
