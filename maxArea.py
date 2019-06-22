import random

def naive(lst):
    water_area = -1
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            _water_area = (j - i)*min(lst[i], lst[j])
            water_area = max(_water_area, water_area)
    return water_area

def two_ptr(height):
    l_ptr, r_ptr = 0, len(height) - 1
    water_area = -1
    while (l_ptr < r_ptr):
        if height[l_ptr] < height[r_ptr]:
            water_area = max((r_ptr - l_ptr) * height[l_ptr], water_area)
            l_ptr += 1
        else:
            water_area = max((r_ptr - l_ptr) * height[r_ptr], water_area)
            r_ptr -= 1
    return water_area

def main():
    num_tests, = map(int, input().split())
    num_range = range(1, 1000)
    for i in range(num_tests):
        lst = random.sample(num_range, 500)
        if two_ptr(lst) == naive(lst):
            print(f"Test {i + 1} passed")
        else:
            print(f"Test {i + 1} failed")
            print(lst)
            print(two_ptr(lst))
            print(naive(lst))
            assert(False)

if __name__ == "__main__": main()
