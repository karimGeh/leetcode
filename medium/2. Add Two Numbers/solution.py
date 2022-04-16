# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = str(l1.val)
    while l1.next != None:
      l1 = l1.next
      a += str(l1.val)

    b = str(l2.val)
    while l2.next != None:
      l2 = l2.next
      b += str(l2.val)

    a = int(a[::-1])
    b = int(b[::-1])

    output = str(a+b)[::-1]

    print(output)

    d = ListNode(val=output[0])
    f = d

    for c in output[1:]:
      f.next = ListNode(val=c)
      f = f.next

    return d
