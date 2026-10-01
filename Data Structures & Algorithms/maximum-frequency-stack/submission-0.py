class FreqStack:

    def __init__(self):
        self.freq = {} 
        self.stack = []

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        frequencyOfVal = self.freq[val]

        while len(self.stack) <= frequencyOfVal:
            self.stack.append([])

        self.stack[frequencyOfVal].append(val)


    def pop(self) -> int:
        while self.stack[-1] == []:
            self.stack.pop()

        res = self.stack[-1].pop()
        self.freq[res] -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()