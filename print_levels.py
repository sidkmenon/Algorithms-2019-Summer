# print each level of a bst
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    @property
    def val(self):
        return self._val
    @val.setter
    def val(self, new_val):
        self._val = new_val
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, new_node):
        self._next = new_node


class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []

def print_levels(root):
    res = []
    current_level = []
    current_level.append(root)
    visited = {}
    while True:
        ll, head = None, None
        next_lst = []
        while len(current_level != 0):
            cn = current_level.pop()
            new_node = Node(cn.val)
            if ll is None:
                head = new_node
            else:
                ll.next = new_node
            ll = new_node
            for child in cn.children:
                if child not in visited:
                    visited[child] = True
                    next_lst.append(child)
        res.append(head)
        if len(next_lst) == 0:
            break
        else:
            current_level = next_lst
    return res


print('Good')
