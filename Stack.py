class Stack:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items:
            self.items.pop()
        else:
            return None
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return self.items == []
            
        

s=Stack()
print(s.is_empty())
s.push('apple')
s.push('papaya')
print(s.items)
s.pop()
s.push('banana')
print(s.items)
print(s.peek())
print(s.size())
print(s.is_empty())