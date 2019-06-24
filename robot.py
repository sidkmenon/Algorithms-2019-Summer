from __future__ import annotations
def main():
    pass

# classic robot problem navigating from top left to bottom right
# of m x n grid. Time complexity: O(mn), Space Complexity: O(min(m, n))
def uniquePaths(m: int, n: int) -> int:
    smaller_dim, bigger_dim = min(m, n), max(m, n)
    stor = [1] * smaller_dim
    for _ in range(1, bigger_dim):
        for i in range(1, smaller_dim):
            stor[i] += stor[i-1]
    return stor[-1]

print(path(7, 3))

if __name__ == "__main__": main()
