from itertools import combinations


class Solution:
  def twoSum(self, nums, target):
    for a, b in combinations(nums, 2):
      if a + b != target:
        continue

      i = nums.index(a)
      j = nums.index(b, i+1)
      return [i, j]
