# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        p = head
        q = head
        for i in range(n):
            head = head.next
        if head == None:         # 如第一个指针提前走了n步到达末尾
            return p.next
        
        while head.next != None:
            head = head.next
            p = p.next
        temp = p.next
        p.next = temp.next
        del temp
        return q     #www.baidu.com
    ##hello world!we rng
