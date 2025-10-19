class BucketedList:
    def __init__(self, numbers, num_buckets=3):
        self.numbers = numbers
        self.num_buckets = num_buckets
        self.buckets = self._make_buckets()

    def _make_buckets(self):
        n = len(self.numbers)
        size = max(1, n // self.num_buckets)
        return [self.numbers[i:i + size] for i in range(0, n, size)]

    def summary(self):
        return [{"min": min(b), "max": max(b), "len": len(b)} for b in self.buckets]

data = [1, 5, 8, 2, 3, 9, 7]
b = BucketedList(data, num_buckets=2)
print(b.summary())
