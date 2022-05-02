class Solution:
  def reverse(self, x: int) -> int:
    a = int(str(abs(x))[::-1])
    if a >= 2147483648:
      return 0
    return a * [-1, 1][x >= 0]
