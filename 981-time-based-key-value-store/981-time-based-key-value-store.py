class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        time_map = self.map.get(key, {})
        time_map[timestamp] = value
        self.map[key] = time_map

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        time_map = self.map[key]
        while timestamp not in time_map and timestamp > 0:
            timestamp -= 1
        if timestamp == 0:
            return ""
        return time_map[timestamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)