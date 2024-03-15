class RecentCounter:

    def __init__(self):
        self.pings =[]

    def ping(self, t: int) -> int:
        # Append the current timestamp to the list
        self.pings.append(t)
        
        # Remove timestamps that are older than 3000 milliseconds (3 seconds)
        while self.pings[0] < t - 3000:
            self.pings.pop(0)
        
        # Return the number of pings within the last 3000 milliseconds
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)