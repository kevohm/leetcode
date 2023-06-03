class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    @classmethod
    def create_from_array(cls, arr):
        current = None
        i = len(arr) - 1
        while i >= 0:
            current = cls(arr[i], current)
            i -= 1
        return current
    def print_nodes(self):
        while self is not None:
            if self.next is None:
                print(self.val)
            else:
                print(self.val, end="->")
            self = self.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = 0
        carry = None
        ans = []
        newNode = None
        while l1 is not None and l2 is not None:
            if carry is not None:
                total = l1.val + l2.val + carry
                carry = None
            else:
                total = l1.val + l2.val
            if(total > 9):
                sum = str(total)
                carry = int(sum[0])
                current = int(sum[1])
                if l1.next is None and l2.next is None:
                    ans.append(current)
                    ans.append(carry)
                elif l1.next is None:
                    ans.append(current)
                else:
                    ans.append(current)
            else:
                ans.append(total)
            l1 = l1.next
            l2 = l2.next
            if l1 is None:
                while l2 is not None:
                    sum = 0
                    if carry is not None:
                        sum = l2.val + carry
                        carry = None
                    else:
                        sum = l2.val
                    if sum > 9:
                        carry = int(str(sum)[0])
                        current = int(str(sum)[1])
                        ans.append(current)
                        if(l2.next is None):
                            ans.append(carry)
                    else:
                        ans.append(sum)
                    l2 = l2.next
            if l2 is None:
                while l1 is not None:
                    sum = 0
                    if carry is not None:
                        sum = l1.val + carry
                        carry = None
                    else:
                        sum = l1.val
                    if sum > 9:
                        carry = int(str(sum)[0])
                        current = int(str(sum)[1])
                        ans.append(current)
                        if(l1.next is None):
                            ans.append(carry)
                    else:
                        ans.append(sum)
                    l1 = l1.next
        i = len(ans) - 1
        while i >= 0:
            newNode = ListNode(ans[i], newNode)
            i -= 1
        return newNode
    
#l1 = [2,4,3], l2 = [5,6,4]
#l1 = [0], l2 = [0]
#l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

l1 = ListNode.create_from_array([5])
l1.print_nodes()

l2 = ListNode.create_from_array([5])
l2.print_nodes()


Solution().addTwoNumbers(l1, l2).print_nodes()