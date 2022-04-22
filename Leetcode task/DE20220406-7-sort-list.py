# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #         if not head:
        #             return None

        #         values = []
        #         while head != None:
        #             values.append(head.val)
        #             head = head.next

        #         values.sort()

        #         nodes = None
        #         for i in values[::-1]:
        #             nodes = ListNode(val=i, next=nodes)

        #         return nodes

        if not head:
            return None

        result = new_node = head

        values = []
        while head != None:
            values.append(head.val)
            head = head.next

        values.sort()

        for num in values:
            new_node.val = num
            new_node = new_node.next

        return result
