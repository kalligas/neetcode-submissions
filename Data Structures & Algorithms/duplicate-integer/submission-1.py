class Hashmap:
    def __init__(self):
        self.size = 8
        self.elements = 0
        self.buckets = [None] * self.size

    @property
    def load_factor(self):
        return self.elements / self.size

    def _hash(self, key):
        return key % self.size

    def contains(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]

        if bucket is None:
            return False

        for existing_key in bucket:
            if existing_key == key:
                return True

        return False

    def add(self, key):
        if self.contains(key):
            return

        hash_key = self._hash(key)

        if self.buckets[hash_key] is None:
            self.buckets[hash_key] = []

        self.buckets[hash_key].append(key)
        self.elements += 1

        if self.load_factor > 0.75:
            self.resize()

    def resize(self):
        old_buckets = self.buckets

        self.size *= 2
        self.elements = 0
        self.buckets = [None] * self.size

        for bucket in old_buckets:
            if bucket is not None:
                for key in bucket:
                    self.add(key)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = Hashmap()
        for num in nums:
            if my_set.contains(num):
                return True
            my_set.add(num)
        return False