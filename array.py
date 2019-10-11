
# quicksort pivot algorithm 
def dutch_national_flag(idx, A): 
    # SMALLER: A[:less_than_idx]
    # EQUAL: A[less_than_idx:b_idx]
    # GREATER: A[larger_than_idx:]
    # UNSORTED: A[b_idx : larger_than_idx]

    pivot_elt = A[idx]
    start_of_eq, current_idx, larger_than_idx = 0, 0, len(A) 
    while current_idx < start_of_larger: 
        if A[current_idx] < pivot_elt: 
            A[current_idx], A[start_of_eq] = A[start_of_eq], A[current_idx]
            current_idx += 1 
            start_of_eq += 1 
        elif A[current_idx] == pivot_elt: 
            current_idx += 1 
        else: 
            larger_than_idx -= 1 
            A[larger_than_idx], A[current_idx] = A[current_idx], A[larger_than_idx] 
    return A 

def update(A): 
    current_idx = len(A) - 1
    A[current_idx] += 1 
    while current_idx > 0:
        div, rem = A[current_idx] // 10, A[current_idx] % 10 
        if div == 0: 
            break 
        else: 
            A[current_idx] = rem 
            current_idx -= 1 
            A[current_idx] += div 
    if A[0] // 10 != 0: 
        div = A[0] // 10
        A[0] //= 10 
        A += [div] + A 
    return A 

print(update([1, 2, 9]))

res = [0, 0, 0, 0, 2, 3]
res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]
print(res)
 
def delete_neighbors(A): 
    if len(A) <= 1:
        return A 
    idx = 1 
    for i in range(1, len(A)): 
        if A[i] != A[idx - 1]:
            A[idx] = A[i]
            idx += 1 
    return A 

print(delete_neighbors([1, 2, 2, 2, 2, 3, 4, 5]))


def max_profit(A): 
    min_price, max_profit = A[0], 0 
    for x in A: 
        min_price = min(min_price, x)
        max_profit = max(max_profit, x - min_price)
    return max_profit 

print(max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))


def buy_sell_2x(A): 
    min_price, max_profit_1_sell, max_profit_2_buy, max_profit = A[0], 0, float('-inf'), 0 
    for p in A: 
        min_price = min(min_price, p) 
        max_profit_1_sell = max(max_profit_1_sell, p - min_price)
        max_profit_2_buy = max(max_profit_2_buy, max_profit_1_sell - p)
        max_profit = max(max_profit, max_profit_2_buy + p) 
    return max_profit

print(buy_sell_2x([12, 11, 13, 9, 12, 8, 14, 13, 15]))
print(buy_sell_2x([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

def lengthOfLongestSubstringKDistinct(s, k):
    b, e, max_len = 0, 0, 0 
    d = {}
    while e < len(s): 
        if s[e] in d: 
            d[s[e]] += 1 
        else: 
            d[s[e]] = 1
        while len(d) > k: 
            d[s[b]] -= 1 
            if d[s[b]] == 0: 
                d.pop(s[b])  
            b += 1 
        e += 1 
        max_len = max(max_len, e - b)
    return max_len 



print(lengthOfLongestSubstringKDistinct("eceba", 2))


