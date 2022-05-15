# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def getlists(self, lis):
    l = []
    if lis != None:
      while lis.next != None:
        l.append(lis.val)
        lis = lis.next
      l.append(lis.val)
    return l

  def mergeKLists(self, lists):
    if len(lists):
      L = [i for sublist in [self.getlists(l) for l in lists] for i in sublist]
      L = sorted(L)
      for i in range(len(L)):
        L[i] = ListNode(L[i])
        if i != 0:
          L[i-1].next = L[i]

      if len(L):
        return L[0]
