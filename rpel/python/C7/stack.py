class stack:

  class node:
    data = None
    pointer = None
  
  stackPointer = None

  def push(self,item):
    #check stack overflow
    try:
      newNode = stack.node()
      newNode.data = item
      newNode.pointer = self.stackPointer
      self.stackPointer = newNode
      return True
    except:
      return False

  def pop(self):
    #check underflow
    if self.stackPointer != None:
      #pop
      popped = self.stackPointer.data
      self.stackPointer = self.stackPointer.pointer
      return popped
    else:
      return None
  
  def peek(self):
    if self.stackPointer != None:
      #peek
      return self.stackPointer.data
    else:
      return None


items = ["one","two", "three", "four"]
s = stack()
for index in range(0, len(items)):
  s.push(items[index])
