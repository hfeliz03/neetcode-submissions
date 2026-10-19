class MyQueue:

    def __init__(self):
        self.write = []
        self.read = []

    def push(self, x: int) -> None:
        self.write.append(x)

    def populateRead(self):
        if not self.read:
            while self.write:
                self.read.append(self.write.pop())

    def pop(self) -> int:
        self.populateRead()
        return self.read.pop()

    def peek(self) -> int:
        self.populateRead()
        return self.read[-1]

    def empty(self) -> bool:
        return not self.read and not self.write