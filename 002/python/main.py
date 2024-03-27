# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_list = temp_list = ListNode()
        # recursive will fail, due to next maybe none 
        while l1 or l2:
            if l1 and l2:
                temp_list.val = temp_list.val + l1.val + l2.val
                l1, l2 = l1.next, l2.next
            elif l1:
                temp_list.val = temp_list.val + l1.val
                l1 = l1.next
            elif l2:
                temp_list.val = temp_list.val + l2.val
                l2 = l2.next
            
            if l1 or l2 or temp_list.val >= 10:
                temp_list.next = ListNode()
                # can use divmod to simplify
                # temp_list.next.val, temp_list.val = divmod(temp_list.val, 10)
                temp_list.next.val = temp_list.val // 10
                temp_list.val = temp_list.val % 10
                temp_list = temp_list.next

        return result_list

def main():
    a, b = ListNode(), ListNode()
    a.val, b.val = 0, 0
    test = Solution()
    test.addTwoNumbers(a, b)

if __name__ == '__main__':
    main()