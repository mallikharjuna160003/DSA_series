class stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self,data):
        self.list.append(data)
        
    def pop(self):
        if self.isEmpty():
            return "Empty list"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        return self.list[len(self.list)-1]
    def delete(self):
        self.list = None

s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(60)
print("peek element",s1.peek())
print(s1)
        
        
