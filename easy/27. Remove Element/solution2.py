import typing


class Solution:
  def removeElement(self, nums: typing.List[int], val: int) -> int:
    while val in nums:
      del nums[nums.index(val)]

    return len(nums)
