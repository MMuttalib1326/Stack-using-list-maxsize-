class stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.list=[]
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        values='\n'.join(values)

# is empty
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False

# is full
    def isfull(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False

# push
    def push(self,value):
        if self.isfull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been succefully inserted"

# pop
    def pop(self):
        if self.isempty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

# peek
    def peek(self):
        if self.isempty():
            return "There is no any element in the stack"
        else:
            return self.list[len(self.list)-1]

# delete 
    def delete(self):
        self.list=None

customstack = stack(4)
#print(customstack.isempty())
#print(customstack.isfull())
customstack.push(1)  
customstack.push(2) 
customstack.push(3)
print(customstack)    


