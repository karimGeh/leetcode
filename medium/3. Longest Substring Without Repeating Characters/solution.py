class Solution(object):
  def lengthOfLongestSubstring(self, s):

    size = min(97, len(s))

    if size == 0:
      return 0

    for w in range(size, 0, -1):
      for l in range(size - w+1):
        sub = s[l:l+w]
        if all(sub.count(c) == 1 for c in sub):
          return w
