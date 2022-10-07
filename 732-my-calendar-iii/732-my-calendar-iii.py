class MyCalendarThree:

    def __init__(self):
        self.bookings = {}
        

    def book(self, start: int, end: int) -> int:
        self.bookings[start] = self.bookings.get(start, 0) + 1
        self.bookings[end] = self.bookings.get(end, 0) - 1
        
        k = 0
        max_k = 0
        for _, val in sorted(self.bookings.items(), key=lambda b: b[0]):
            k += val
            max_k = max(max_k, k)
        return max_k
            
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)