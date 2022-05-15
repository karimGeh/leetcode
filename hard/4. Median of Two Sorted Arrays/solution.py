import statistics


class Solution:
  def findMedianSortedArrays(self, nums1, nums2) -> float:
    return statistics.median(nums1+nums2)
