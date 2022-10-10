# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if (head != None):
            # Saving the head in current to keep track of the position
            current = head

            # Loop continues till the next item on the list is None 
            while (current.next != None):
                # Removing the next item in the list if it is duplicate
                if (current.val == current.next.val):
                    current.next = current.next.next
                # Moving to the next item if no duplicates are found.
                else:
                    current = current.next
        
        return head