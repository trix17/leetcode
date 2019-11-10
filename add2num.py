# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        newList = ListNode(0)
        temp = newList
        totalSum = 0
        
        while l1 or l2 or carry:
            if l1:
                totalSum += l1.val
                l1 = l1.next
            if l2:
                totalSum += l2.val
                l2 = l2.next  
                
            totalSum += carry
            temp.next = ListNode(totalSum % 10)
            carry = totalSum // 10
            totalSum = 0
            temp = temp.next
            
        return newList.next
            
