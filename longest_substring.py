from __future__ import annotations

def lengthOfLongestSubstring(s: str) -> int:
    most_recently_seen = {}
    max_length = 0
    start = -1
    for i in range(len(s)):
        if s[i] in most_recently_seen and start < most_recently_seen[s[i]]:
            start = most_recently_seen[s[i]]
        most_recently_seen[s[i]] = i
        max_length = max(i - start, max_length)
    return max_length

def main():
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
# A B B A
# 0 0 1      start
# 0 1 2      most recently seen
# 1 2 1      max length

# A B C D E C
# 0 1 2 3 4 5


if __name__ == "__main__": main()
