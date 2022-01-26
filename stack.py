#stack implimentation

class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def empty(self):
        if not self.stack:
            return True
        else:
            return False

    def print(self):
        print(self.stack)



stack = Stack()
print(stack.empty())
stack.push(3)
print(stack.empty())
stack.push(2)
stack.print()
print(stack.peek())
stack.pop()
stack.print()