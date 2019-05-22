from __future__ import annotations
import numpy as np

def main():
    num_tests, = map(int, input().split())
    for i in range(num_tests):
        array_1 = sorted([np.random.randint(-50, 51) for _ in range(np.random.randint(1, 100))])
        array_2 = sorted([np.random.randint(-50, 51) for _ in range(np.random.randint(1, 100))])
        ans, merged_lst = combine(array_1, array_2)
        fast_ans = findMedianSortedArrays(array_1, array_2)
        if fast_ans == ans:
            print("test {0} passed".format(i + 1))
        else:
            print("test {0} failed".format(i + 1))
            print("median_ans: {0}, correct_ans: {1}".format(fast_ans, ans))
            print("array 1: {0}".format(array_1))
            print("array 2: {0}".format(array_2))
            print("merged list: {0}".format(merged_lst))
            exit()

def combine(l1: List[int], l2: List[int]) -> float:
    def median(lst: List[int]) -> float:
        n = len(lst)
        if n % 2 == 0:
            return 0.5 * (lst[n//2 - 1] + lst[n//2])
        else:
            return 1.0 * lst[n//2]
    i = 0
    j = 0
    tot = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            tot.append(l1[i])
            i += 1
        else:
            tot.append(l2[j])
            j += 1
    while j < len(l2):
        tot.append(l2[j])
        j += 1
    while i < len(l1):
        tot.append(l1[i])
        i += 1
    return median(tot), tot


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def median(lst: List[int]) -> float:
        n = len(lst)
        if n % 2 == 0:
            return 0.5 * (lst[n//2 - 1] + lst[n//2])
        else:
            return 1.0 * lst[n//2]
    def bounds(min_len, median_index, l):
        lower_bound = max(0, median_index - (min_len + 1)//2)
        upper_bound = min(l-1, median_index + (min_len + 1)//2)
        return lower_bound, upper_bound
    m, n = len(nums1), len(nums2)
    if m == 0:
        return median(nums2)
    elif n == 0:
        return median(nums1)
    else:
        median = lambda l: (l - 1)//2
        smaller_len = min(m, n)
        lb, ub = bounds(smaller_len, median(m), m)
        if lb > ub:
            lb = ub
        median_val, found_median = findMedian(nums1, nums2, lb, ub)
        if not found_median:
            lb, ub = bounds(smaller_len, median(n), n)
            median_val, found_median = findMedian(nums2, nums1, lb, ub)
        return median_val

def evaluate_median_pair(total_length: int, left: int, r1:int , r2: int) -> float:
    assert(r1 is not None or r2 is not None)
    if total_length%2 == 0:
        if r2 is None or (r1 is not None and r1 <= r2):
            return 0.5 * (left + r1)
        else:
            return 0.5 * (left + r2)
    else:
        return left

# binary search through "search" lst looking for a suitable median (by checking in lst)
# look from lb -> ub
def findMedian(search: List[int], lst: List[int], lb: int, ub: int) -> (float, bool):
    n, m = len(search), len(lst)
    target_num_elements_less = (n + m) // 2
    leftover = (m + n) % 2
    while (lb <= ub):
        median_index = (lb + ub)//2
        element_to_right = search[median_index + 1] if median_index <= n - 2 else None
        implied_lst_index = target_num_elements_less - (median_index + (1 - leftover)) - 1
        if implied_lst_index < -1: # median too high
            ub = median_index - 1
        elif implied_lst_index == -1: # no element on the left to check
            if search[median_index] <= lst[0]:
                median = evaluate_median_pair(m + n, search[median_index], element_to_right, lst[0])
                return median, True
            else:
                ub = median_index - 1
        elif implied_lst_index > m - 1: # median too low
            lb = median_index + 1
        elif implied_lst_index == m - 1: # no element on the right to check:
            if search[median_index] >= lst[m-1]:
                median = evaluate_median_pair(m + n, search[median_index], element_to_right, None)
                return median, True
            else:
                lb = median_index + 1
        else:
            if search[median_index] >= lst[implied_lst_index]:
                if search[median_index] <= lst[implied_lst_index + 1]:
                    median = evaluate_median_pair(m + n, search[median_index], element_to_right, lst[implied_lst_index + 1])
                    return median, True
                else:
                    ub = median_index - 1
            else:
                lb = median_index + 1
    return None, False

if __name__ == "__main__": main()
