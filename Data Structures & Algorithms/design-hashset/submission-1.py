class MyHashSet:

    def __init__(self):
        self.vec = []

    def add(self, key: int) -> None:
        if key not in self.vec:
            self.vec.append(key)

    def remove(self, key: int) -> None:
        if key in self.vec:
            i = self.vec.index(key)
            self.vec.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.vec


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)