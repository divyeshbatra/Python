class Stack:
    def __init__(self):
        self.items=[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
            return self.items.pop()
        
    def is_empty(self):
        return self.items==[]
            
def match_symbol(symbol_str):
    symbol_pairs={'(':')','[':']','{':'}'}
    
    openers=symbol_pairs.keys()
    s=Stack()
  

    i=0

    while i<len(symbol_str):
        symbol=symbol_str[i]
    
        if symbol in openers:
            s.push(symbol)
        else:
            if s.is_empty()==True:
                return False
            
            else:
                topsymbol=s.pop()
                if symbol!=symbol_pairs[topsymbol]:
                    return False
                
        i=i+1
    if s.is_empty() == True:
        return True
    return False

print('db')
print(match_symbol('[()]'))




        