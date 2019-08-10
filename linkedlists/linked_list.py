class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
    
class Linkedlist:
  def __init__(self):
    self.head = None
  
  # Insert element at start of the linked list
  def prepend(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node      
   #self.head = Node(data, self.head)
    else:
      new_node.next = self.head
      self.head = new_node
    
  # Insert element at end of the linked list
   def append(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node   
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
        
  # Insert element at nth position of linked list
    def insert_nth(self, data, position):
      new_node = Node(data)
      
      if position == 0 or self.head is None:
        new_node.next = self.head
        self.head = new_node
      else:
        count = 1
        current = self.head
      
      while current.next and count < position:
        current = current.next 
        count += 1
      new_node.next = current.next
      current.next = new_node
      
      
      
        
        
      
