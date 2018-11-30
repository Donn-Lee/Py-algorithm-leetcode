# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #slow : x + y + mc
        #fast: x + y + nc (c是cicle的长度, y + z = c, y 是meet时距离cicle起点的距离)
        #fast = 2 * slow => x + y = (n-2m)C => x + y = (n-2m-1)c + y+z => x = kc + z （k可正可负）
        #让一个指针从原点走，一个从相遇的点走，碰到的node就是cicle的起点

        
        slow, fast = head,head
        meet = False
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
            if slow == fast:
                meet = True
                break
        if not meet:
            return None
        #slow 现在是相遇的点
        else:
            while head!=slow:
                head,slow = head.next,slow.next
            return head
