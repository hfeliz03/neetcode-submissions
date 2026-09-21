class StockSpanner:
    def __init__(self):
        self.daysAndSpans = []

    def next(self, price: int) -> int:
        self.daysAndSpans.append([price, 1])
        i = len(self.daysAndSpans) - 2
        while i >= 0:
            if price >= self.daysAndSpans[i][0]: 
                self.daysAndSpans[-1][1] += self.daysAndSpans[i][1]
                i -= self.daysAndSpans[i][1]
            else: break
            
        return self.daysAndSpans[-1][1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)