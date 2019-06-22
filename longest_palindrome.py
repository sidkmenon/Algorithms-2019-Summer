def main():
    print(longestPalindrome("aaaa"))
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


if __name__ == "__main__": main()
