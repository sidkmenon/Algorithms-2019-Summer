
def smallest_difference(lst):
    def to_int(time_str):
        return int(time_str[0:2]) * 60 + int(time_str[3:])
    if len(lst) <= 1:
        raise ValueError("No smallest difference")
    lst = list(map(to_int, lst)) # in place
    lst.sort()
    lst.append(24 * 60 + lst[0])
    m = float("inf")
    for i in range(1, len(lst)):
        m = min(lst[i] - lst[i-1], m)
    return m

print(smallest_difference(["09:30", "10:46", "23:59", "00:00"]))
