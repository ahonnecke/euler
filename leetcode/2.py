# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def arrayToNumber(self, number):
        out = 0
        ix = 0
        node = number
        while node != None:        
            out += node.val * (10**ix)
            ix += 1
            node = node.next
        return out
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = self.arrayToNumber(l1) + self.arrayToNumber(l2)

        arrout = []
        string = str(out)
        for i in range(len(string)):
            arrout.insert(0, int(string[i]))
        return arrout

n3 = ListNode(3)
n2 = ListNode(4)
n1 = ListNode(2)
n1.next = n2
n2.next = n3

n6 = ListNode(4)
n5 = ListNode(6)
n4 = ListNode(5)
n4.next = n5
n5.next = n6

s = Solution()
#print(s.addTwoNumbers([2,4,3], [5,6,4]))
print(s.addTwoNumbers(n1, n4))

