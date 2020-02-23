class LinkedList:
  def __init__(self, obj=None):
    self.head = None
    if isinstance(obj, Node):
      self.head = obj
    elif isinstance(obj, LinkedList):
      self.head = obj.head
    self.print = self.printlist

  def appendAll(self, *data):
    for d in data:
      self.append(d)

  def append(self, data):
    current = self.head
    while current and current.next:
      current = current.next
    if not current:
      self.head = Node(data)
    else:
      current.next = Node(data)

  def prepend(self, data):
    self.head = Node(data, self.head)
  
  def printlist(self):
    current = self.head
    ans = []
    while current:
      ans.append(current.data)
      current = current.next
    print(ans)
  
  def split(self):
    slow = fast = self.head
    while fast and fast.next:
      fast = fast.next.next
      if not fast:
        break
      slow = slow.next

    head2 = None
    if slow:
      head2 = slow.next
      slow.next = None
    return LinkedList(head2)

  def sort(self):
    tail = self.split()
    if tail.head:
      self.sort()
      tail.sort()
      self.merge_sorted_lists(tail)

  def merge_sorted_lists(self, other_list):
    merge_sorted_lists(self, other_list)

# split_list splits a list and returns 2 sublists 
def split_list(ls):
  tail = ls.split()
  return ls, tail

def merge_sorted_lists(l1, l2):
  ptr1 = l1.head
  ptr2 = l2.head
  ptr4 = ptr3 = Node('dummy')
  while ptr1 and ptr2:
    if ptr1.data < ptr2.data:
      ptr3.next = ptr1
      ptr1 = ptr1.next
    else:
      ptr3.next = ptr2
      ptr2 = ptr2.next
    ptr3 = ptr3.next
  ptr3.next = ptr1 or ptr2
  l1.head = ptr4.next
  l2.head = None

def merge_sort(ls):
  if ls.head and ls.head.next:
    h, t = split_list(ls)
    merge_sort(h)
    merge_sort(t)
    merge_sorted_lists(h, t)

class Node:
  def __init__(self, data, next = None):
    self.data = data 
    self.next =  next
  

# ll = LinkedList()
# ll.append(5)
# ll.append(6)
# ll.append(7)
# ll.append(4)
# ll.printlist()

# l2 = LinkedList(ll)
# l2.prepend(3)
# l2.prepend(1)
# l2.append(10)
# l2.append(12)
# print('+' * 40)
# l2.printlist()
# print('-' * 40)
# l3 = l2.split()
# l2.print()
# l3.print()

l1 = LinkedList()
l1.appendAll(7, 1, 2, 4, 3, 6, 5, -2, -3)
l1.sort()
l1.print()
