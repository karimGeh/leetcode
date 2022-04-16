class Solution:
  def romanToInt(self, s: str) -> int:
    d = [
        ['IV', ' 4 '],
        ['IX', ' 9 '],
        ['XL', ' 40 '],
        ['XC', ' 90 '],
        ['CD', ' 400 '],
        ['CM', ' 900 '],
        ["I", " 1 "],
        ["V", " 5 "],
        ["X", " 10 "],
        ["L", " 50 "],
        ["C", " 100 "],
        ["D", " 500 "],
        ["M", " 1000 "],
    ]
    for a, b in d:
      s = s.replace(a, b)
    s = s.split()
    return sum(map(int, s))
