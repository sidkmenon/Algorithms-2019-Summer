import functools
import random
import string 

def string_to_int(s): 
    is_negative = s[0] == "-"
    return (-1 if is_negative else 1) * functools.reduce(lambda acc, c: acc * 10 + string.digits.index(c), 
                                                       s[is_negative:], 0)

print(string_to_int("20202020"))

def test_string(num_iters):
    for _ in range(num_iters): 
        sd = random.randint(-10000, 10000)
        try:
            assert(sd == string_to_int(str(sd)))
        except: 
            print(sd)
    return 'passed'

num_tests = 10000
print(f'{num_tests} test cases of test string: {test_string(num_tests)}')


def string_to_base(s): 
    pass 


def quickselect(A, k): 
    def __partition(A, start, end, p_idx): 
        if len(A) <= 1: 
            return p_idx 
        A[end], A[p_idx] = A[p_idx], A[end]
        # A[:le] less than or equal 
        # A[gt:] greater than 
        le, gt = 0, end 
        while le < gt: 
            if A[le] <= A[end]: 
                le += 1 
            else: 
                gt -= 1 
                A[gt], A[le] = A[le], A[gt]
        A[gt], A[end] = A[gt], A[end]
        return gt
    start, end = 0, len(A) - 1
    while start <= end: 
        r_idx = random.randint(start, end)
        p_idx = __partition(A, start, end, r_idx)
        if p_idx == k - 1: 
            return A[:k]
        elif p_idx < k - 1: 
            start = p_idx + 1 
        else: 
            end = p_idx - 1 
    return None 


# def quickselect(A, k): 
#     def __partition(A, start, end, p_idx): 
#         # invariants: A[:s] < A[p_idx]
#         # Invariant A[s:e]
#         if len(A) <= 1: 
#             return p_idx 
#         A[end], A[p_idx] = A[p_idx], A[end] 
#         s, e, l = start, start, end
#         while e < l: 
#             if A[e] < A[end]: # partition element 
#                 A[s], A[e] = A[e], A[s]
#                 e += 1 
#                 s += 1 
#             elif A[e] == A[end]: 
#                 e += 1
#             else:
#                 l -= 1 
#                 A[l], A[e] = A[e], A[l]
#         A[l], A[end] = A[end], A[l]
#         return l 
#     start, end = 0, len(A) - 1
#     while True: 
#         p_idx = random.randint(start, end)
#         new_idx = __partition(A, start, end, p_idx)
#         if new_idx == k - 1: 
#             return A[:k]
#         elif new_idx > k - 1: 
#             end = new_idx - 1 
#         else: 
#             start = new_idx + 1
        
print(quickselect([5, 4, 3, 2, 1, 0, -1, 40], 3))

# print(quickselect([0, 1, 2], ))

import collections 
def removeInvalidParentheses(s): 
        def is_valid(paren_expr): 
            lstack = 0 
            for c in paren_expr: 
                if c == "(": 
                    lstack += 1 
                elif c == ")": 
                    lstack -= 1
                    if lstack < 0: 
                        return False 
            return (lstack == 0)
        queue = collections.deque()
        queue.appendleft(s)
        visited = collections.defaultdict(bool)
        while len(queue) > 0: 
            current_str = queue.pop()
            visited[current_str] = True 
            if is_valid(current_str): 
                print(list(queue))
                return list(filter(is_valid, queue)) + [current_str]
            else: 
                for i in range(len(current_str)): 
                    new_str = current_str[:i] + current_str[i+1:] 
                    if not visited[new_str]: 
                        queue.appendleft(new_str)
        return [""]

print(removeInvalidParentheses("()())()"))