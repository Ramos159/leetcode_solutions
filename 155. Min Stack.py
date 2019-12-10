# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# Success:

# Runtime: 56 ms, faster than 96.79% of Python3 online submissions for Min Stack.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Min Stack.

class MinStack:

    def __init__(self):
        self.body = []
        self.min = None
        

    def push(self, x: int) -> None:
        self.body.append(x)
        
        if(self.min == None or x < self.min):
            self.min = x

    def pop(self) -> None:
        num = self.body.pop()
        try:
            self.min = min(self.body)
        except ValueError:
            self.min = None
            
        return num
    
    def top(self) -> int:
        return self.body[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Explanation: 

# This is basically designing a stack that supports a weird min function.
# List's make good stacks because of constant push and append time.
# A stack also follows last in first out, which is something a List excels at thanks to the functions mentioned above.
# push() is easy just use the list append method and check if our x parameter should be the new min
# pop() is the same thing except with a caveat, we have to check if the stack is empty to assign min the value of None.
# top() also pretty easy, just return the last element in the self.body list.
# Since min is a variable we hold we can just return it when we call getMin().

# Complexities: 

# Space: O(1), the functions don't add to the space of the stack. just performs operations
# Time: O(1), all functions as well remain constant with no looping just checks and insertions.

########################IMPORTANT_NOTE#####################################################################################################################################

# there is actually a much simpler looking version i've done but for some reason it runs much more slowly on leetcode. something like 800ms compared to the one above.
# Incase you want to see that version I'll put it below.

class MinStack:

    def __init__(self):
        self.body = []
        
    def push(self, x: int) -> None:
        self.body.append(x)

    def pop(self) -> None:
        return self.body.pop()
    
    def top(self) -> int:
        return self.body[-1]

    def getMin(self) -> int:
        return min(self.body)

# In this version you dont keep min somewhere, just return it in the min of the body with the min() function.
# this way we dont need to check for min everytime, just use the min() function.
# this is probably the most clean solution there is but for some reason runs super slow on leetcode. maybe its the built in methods? 
# it's quite ludicrous that it would seem this would be the faster solution but it isnt the case haha. 
# the space percentile remains the same also, thats the funny part. 