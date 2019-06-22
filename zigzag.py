from __future__ import annotations

def convert(s: str, numRows: int) -> str:
  lst = []
  index = 0
  incrementing = False
  for i in range(len(s)):
      if index == 0 or index == numRows - 1:
          incrementing = not incrementing
      lst.append((s[i], index))
      if incrementing:
          index += 1
      else:
          index -= 1
  res = ""
  # if len(s) > 0:
  lst.sort(key=lambda tup: tup[1])
  str_lst, _ = zip(*lst)
  return "".join(str_lst)

def convert2(s: str, numRows: int) -> str:
    if numRows == 1 or len(s) <= 1:
        return s
    lst = []
    incr = 2 * (numRows - 1)
    n = len(s)
    def append_valid(ix, lst, dict_lst):
        if 0 <= ix < n:
            lst.append(s[ix])
            dict_lst.append(ix)
    dict = {}
    for row in range(numRows):
        dict[row] = []
        index = 0
        while index - row < n:
            if 0 < row < numRows - 1:
                append_valid(index - row, lst, dict[row])
            append_valid(index + row, lst, dict[row])
            index += incr
    print(dict)
    return "".join(lst)


print(convert("PAYPALISHIRING", 3))
print(convert2("ABCD", 3))
