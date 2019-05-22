
import numpy as np

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def _addTwoNumbers(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if l1 is None and l2 is None:
            return None
        l1_next = l1.next if l1 is not None else None
        l2_next = l2.next if l2 is not None else None
        v = carry
        if l1 is not None:
            v += l1.val
        if l2 is not None:
            v += l2.val
        new_node = ListNode(v % 10)
        new_node.next = _addTwoNumbers(l1_next, l2_next, v // 10)
        return new_node
    return _addTwoNumbers(l1, l2, 0)

def to_int(x: ListNode):
    def _to_int(x: ListNode, carry: int):
        if x is not None:
            return carry*x.val + _to_int(x.next, carry*10)
        else:
            return 0
    return _to_int(x, 1)


def main():
    sz, = map(int, input().split())
    l1 = ListNode(np.random.randint(0, 9))
    l2 = ListNode(np.random.randint(0, 9))
    count = 1
    n1, n2 = 0, 0
    if sz < 1:
        print("Not a valid size")
        exit()
    x = l1
    y = l2
    for _ in range(sz - 1):
        n1 += count * x.val
        n2 += count * y.val
        x.next = ListNode(np.random.randint(0, 9))
        y.next = ListNode(np.random.randint(0, 9))
        x = x.next
        y = y.next
        count *= 10
    print(n1, to_int(l1))
    print(n2, to_int(l2))
    print(n1 + n2, to_int(addTwoNumbers(l1, l2)))

main()
