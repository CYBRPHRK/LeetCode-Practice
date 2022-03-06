# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Saving the head
        head = l1
        carry = 0

        # Adding the first ListNodes for l1 and l2
        sum = l1.val + l2.val
        if (sum > 9):
            sum = sum % 10
            carry = 1
        l1.val = sum

        # Adding ListNodes for l1 and l2 until one of the Linked Lists finishes
        while (l1.next != None) and (l2.next != None):
            l1 = l1.next
            l2 = l2.next
            sum = l1.val + l2.val + carry
            if (sum > 9):
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            l1.val = sum
            
        # Adding if l1 linked list still has values in it and carry is 1
        while (l1.next != None) and (carry == 1):
            l1 = l1.next
            sum = l1.val + carry
            if (sum > 9):
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            l1.val = sum
        
        # Adding if l2 linked list still has values in it and carry is 1
        while (l2.next != None) and (carry == 1):
            l2 = l2.next
            sum = l2.val + carry
            if (sum > 9):
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            l1.next = ListNode(sum)
            l1 = l1.next
            
        # Adding if l2 linked list still has values in it but carry is 0
        if (l2.next != None):
            l2 = l2.next
            l1.next = l2
            
        # Adding carry if both Linked lists are finished but carry is still 1
        if (carry == 1):
            l1.next = ListNode(carry)
        return head
        