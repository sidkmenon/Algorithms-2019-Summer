# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}
        

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         trie_level = self.trie
#         if not word or len(word) < 0: 
#             return 
#         for i, c in enumerate(word): 
#             if i != len(word) - 1: 
#                 if c not in trie_level: 
#                     trie_level[c] = {}
#                 trie_level = trie_level[c]
#             else: 
#                 trie_level[c] = "STOP"
        
        

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """
#         def __search_subtrie(w, trie): 
#             print(w, trie)
#             if not w: 
#                 return True 
#             for i, c in enumerate(w): 
#                 if not trie: 
#                     return False 
#                 if c == ".": 
#                     return any((__search_subtrie(w[i+1:], subtrie) 
#                                 for subtrie in trie.values()))
#                 else: 
#                     if c not in trie: 
#                         return False 
#                 trie = trie[c]
#             return True 
#         return __search_subtrie(word, self.trie)

 

from __future__ import annotations
import collections 

Trie_Level = collections.namedtuple('Trie_Level', ('end_marker', 'further_letters'))

class Trie:
    def __init__(self): 
        self.trie = {}
        self.END = "STOP"


    # DESIRED STRUCTURE {"x" : { "y" : {}}, "y" : }

    def addWord(self, word : str) -> None : 
        t_iter = self.trie 
        for c in word:
            if c not in t_iter: 
                t_iter[c] = {}
            t_iter = t_iter[c]
        t_iter[self.END] = self.END

    def search(self, word: str) -> bool: 
        def __search_in_trie(idx, trie): 
            if idx == len(word): 
                return self.END in trie
            if word[idx] == ".": 
                return any((__search_in_trie(idx + 1, next_trie) for next_trie in trie.values()))
            else: 
                if word[idx] in trie: 
                    return __search_in_trie(idx + 1, trie[word[idx]])
                return False
        return __search_in_trie(0, self.trie)
                




wd = Trie()

wd.addWord("ba")
wd.addWord("b")
wd.addWord("bad")
wd.addWord("daddy")
wd.addWord("dad")
wd.addWord("mad")

print(wd.trie)

# print("SEARCHING")
print(wd.search("pad"))
print(wd.search("bad"))
print(wd.search(".ad"))
print(wd.search("b.."))
wd.addWord("bx")

wd.addWord("as")
print(wd.search("a"))
print(wd.search("a."))