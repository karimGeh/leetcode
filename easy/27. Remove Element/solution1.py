import typing


class Solution:
  def removeElement(self, nums: typing.List[int], val: int) -> int:
    i = 0
    for _ in range(len(nums)):
      if nums[i] == val:
        del nums[i]
      else:
        i += 1

    return len(nums)
