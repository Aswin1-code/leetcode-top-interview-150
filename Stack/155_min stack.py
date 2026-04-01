class MinStack:

    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Min stack to store the current minimum at each level
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # The new minimum is either the new value or the previous minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
