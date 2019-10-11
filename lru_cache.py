from __future__ import annotations

# doubly linked list
# doubly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedLst:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_head(self, n):
        n.next = self.head
        n.prev = None
        if self.head:
            self.head.prev = n
        else:
            self.tail = n
        self.head = n

    def insert_at_tail(self, n):
        n.next = None
        n.prev = self.tail
        if self.tail:
            self.tail.next = n
        else:
            self.head = n
        self.tail = n

    def remove(self, n):
        if n.next: # if n is not the tail
            n.next.prev = n.prev
        else:
            self.tail = n.prev
        if n.prev: # if n is not the head
            n.prev.next = n.next
        else:
            self.head = n.next


class LRUCache:

    def __init__(self, capacity: int):
        self.current_size = 0
        self.capacity = capacity
        self.d = {}
        self.linkedlst = None # linked list

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self.linkedlst.remove(n)
            self.linkedlst.insert_at_tail(n)
            return n.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.get(key)
            self.d[key].val = (key, value)
            return
        if self.linkedlst:
            if self.current_size < self.capacity:
                self.current_size += 1
            else:
                head_key = self.linkedlst.head.val[0]
                self.linkedlst.remove(self.linkedlst.head)
                self.d.pop(head_key, None)
        else:
            self.linkedlst = LinkedLst()
            self.current_size += 1
        self.linkedlst.insert_at_tail(Node((key, value)))
        self.d[key] = self.linkedlst.tail


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)   # should evict 2
cache.get(2)       # should return -1
cache.put(4, 4)    #// evicts key 1
cache.get(1)      # // returns -1 (not found)
cache.get(3) #      // returns 3
cache.get(4) #       // returns 4

# different short problem -- just hashing tuples

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
        counts = {}
        for a,b in dominoes:
            if (a, b) in counts.keys():
                counts[(a, b)] += 1
            elif (b, a) in counts.keys():
                counts[(b, a)] += 1
            else:
                counts[(a, b)] = 1
        values = list(counts.values())
        num_pairs = [n * (n - 1)/2 for n in values]
        return int(sum(num_pairs))
dominoes = [[1,2],[2,1],[3,4],[5,6]]


numEquivDominoPairs(dominoes)


import functools

def spreadsheet_to_int(col):
    return functools.reduce(lambda acc, c: acc * 26 + ord(c) - ord('A') + 1, col, 0)

import string

string.hexdigits

def int_to_spreadsheet(x):
    acc = []
    while x > 0:
        x -= 1
        acc.append(chr(ord('A') + x % 26))
        x //= 26
    return "".join(reversed(acc))

int_to_spreadsheet(702)



# simple caesar's cipher
def encrypt_cipher(s, offset):
    cipher_result = []
    for i in range(len(s)):
        if s[i].isalpha():
            first_char = 'a' if s[i].islower() else 'A'
            cipher_result.append(chr(ord(first_char) + \
                                (ord(s[i]) - ord(first_char) + offset) % 26))
        else:
            cipher_result.append(s[i])
    return "".join(cipher_result)

# decrypting is the same as encrypting but with negative offset
def decrypt_cipher(s, offset):
    return encrypt_cipher(s, -offset)

encrypt_cipher("abcdefghijklmnopqrstuvwxyz2", 1)


a, b = map(int, input().split())
print(f'I am fucked, ayy{a * b}')
