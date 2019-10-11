def main():
    test = "abba"
    print(longestPalindrome(test))
    print(manachers(test))
def longestPalindrome(s: str) -> str:
    X = [[False for _ in range(len(s))] for _ in range(len(s))]
    start, end = 0, -1
    num_in_middle = lambda i, j : j - i - 1
    for i in reversed(range(len(s))):
        for j in range(i, len(s)):
            if (s[i] == s[j]) and (num_in_middle(i, j) <= 1 or X[i+1][j-1]):
                X[i][j] = True
                if j - i > end - start:
                    start, end = i, j
    return s[start:end+1]


class T:
    def __init__(self, s, spacer='#'):
        self.s = s
        self.spacer = spacer
    def get(self, i):
        if i % 2 == 0:
            return self.spacer
        else:
            return self.s[i // 2]
    def __len__(self):
        return 2*len(self.s) + 1
    def __str__(self):
        return "".join([self.get(i) for i in range(len(self))])

def manachers(s: str) -> str:
    t = T(s)
    c, r, radius = 0, -1, 0
    P = [0] * len(t)
    for i in range(1, len(t)):
        rad = min(P[2*c - i], r - i) if i <= r else 0
        while (i + rad < len(t) and i - rad > 0 and t.get(i - rad) == t.get(i + rad)):
            rad += 1
        P[i] = rad
        if (i + rad - 1 > r):
            c = i
            r = i + rad - 1
    print(P)
    print(t)

if __name__ == "__main__": main()
