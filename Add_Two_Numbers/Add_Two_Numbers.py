class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_nodes(self):
        while self is not None:
            print(self.val)
            self = self.next
n_2 = ListNode(2)
n_l = ListNode(1,n_2)

## code

l1 = [2,4,3]
l2 = [5,6,4]
# [7,0,8]

