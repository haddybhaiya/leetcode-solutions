# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next
        f = []
        m = []
        for i in range(len(l)):
            if i%2==0:
                f.append(l[i])
            else:
                m.append(l[i])
        f=f[:]+m[:]


        for i in range(len(f) - 1):
            f[i].next = f[i+1]

        if f:
                f[-1].next = None
                return f[0]

        return None