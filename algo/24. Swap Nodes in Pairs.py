'''Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''
# 思路 1->2->3->4 添加一个root: root->1->2->3->4 变成 root ->2 ->1->3->4 
#然后在将root=root.next.next 也就是现在的1，在操作3，4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #新建一个头指针指向head
        root = ListNode(0)
        root.next = head
        curr = root
        #当指针1和2存在时
        while curr.next and curr.next.next:
            p1 = curr.next
            p2 = curr.next.next
            #print(root.next.val)
            curr.next = p2
            #print(root.next.val) # 改变curr的属性next root也会跟着改变
            #将1->3
            p1.next = p2.next 
            #将2->1
            p2.next = p1
            #root 变成p1: p2 -> root -> p3 -> p4
            curr = curr.next.next#curr 被赋值到新的对象,此时root不会变，且和curr无关了

        return root.next

a = ListNode(1)
b = ListNode(2)

a.next = b

s = Solution()
s.swapPairs(a)