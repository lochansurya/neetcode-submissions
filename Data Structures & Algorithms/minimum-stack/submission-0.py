class MinStack:

    def __init__(self):
        self.top_index = 0
        self.stack = []
        infinity = sys.maxsize
        self.minimum = infinity

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_index += 1
        self.minimum = min(self.minimum, val)

    def pop(self):
        self.stack.pop()
        self.top_index -= 1

        if self.stack:
            self.minimum = min(self.stack)
        else:
            self.minimum = sys.maxsize

    def top(self) -> int:
        return self.stack[self.top_index - 1]

    def getMin(self) -> int:
        return self.minimum
