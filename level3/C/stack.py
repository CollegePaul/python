#stack example
class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self,item):
        self.stack.append[item]
    
    def pop(self):
        return self.pop()
    
    def peek(self):
        return self.stack[len(self.stack - 1)]
    
    def is_empty(self):
        if len(self.stack)<1:
            return True
        else:
            return False


mystack = Stack()
mystack.push(10)
print(mystack.peek())
print(mystack.is_empty())
print(mystack.pop())
print(mystack.is_empty())

