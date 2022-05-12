class Solution(object):
  def isNumber(self, s):
    try:
      float(s)
      return s.lower().count('e') == sum([c.isalpha() for c in s])
    except:
      return False
