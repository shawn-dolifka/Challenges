'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

#========================================#

class node:
    def __init__(self, v, m):
        self.value = v
        self.node_min = m

    def nodeMin(self):
        return self.node_min

    def nodeVal(self):
        return self.value

#========================================#

class MinStack:

    def __init__(self):
        self.stack = []

#--------------------------#

    def push(self, x):
        if not self.stack:
            new_node = node(x,x)
            self.stack.append(new_node)
        elif self.stack[-1].nodeMin() >= x:
            new_node = node(x,x)
            self.stack.append(new_node)
        else:
            new_node = node(x,self.stack[-1].nodeMin())
            self.stack.append(new_node)

"""
:type x: int
:rtype: void
"""

#--------------------------#

    def pop(self):
        self.stack.pop()

"""
:rtype: void
"""

#--------------------------#

    def top(self):
        top = self.stack[-1:]
        return top[0].nodeVal()

"""
:rtype: int
"""

#--------------------------#

    def getMin(self):
        mini = self.stack[-1:]
        return mini[0].nodeMin()

"""
:rtype: int
"""

'''
I'll write a main body some other time. Works on Leetcode.
'''