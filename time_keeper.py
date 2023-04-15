import time


class TimeKeeper:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        elapsed_time = self.end - self.start
        print(f"With bloğunun içindeki işlemler {elapsed_time:.4f} saniyede tamamlandı.")


with TimeKeeper():
    total = 0
    for i in range(20000000):
        total += i
    print(total)