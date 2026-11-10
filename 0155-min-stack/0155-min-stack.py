class MinStack:

    def __init__(self):
        self.stack=[]
        self.m=float('inf')
        self.t=-1

    def push(self, value: int) -> None:
        self.t+=1
        self.m = min(value, self.m)
        self.stack.append((value, self.m))

    def pop(self) -> None:
        self.t -= 1
        self.stack.pop()
        self.m = float('inf') if self.t==-1 else self.stack[self.t][1] 

    def top(self) -> int:
        return self.stack[self.t][0]
        
    def getMin(self) -> int:
        return self.m



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()