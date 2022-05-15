# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
  def reverseKGroup(self, head, k):
    if k <= 1:
      return head

    toList = [head.val]
    tail = head
    while tail.next:
      tail = tail.next
      toList += [tail.val]

    size = len(toList)
    for i in range(0, size, k):
      if i+k > size:
        continue
      toList[i:i+k] = toList[i:i+k][::-1]

    tail = head
    i = 0
    while tail:
      tail.val = toList[i]
      tail = tail.next
      i += 1

    return head
