from itertools import product
import time

if __name__ == "__main__":
    ls = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    start = time.perf_counter_ns()
    for _ in range(10000):
        total = 0
        for idx in product(range(3), range(4)):
            total += ls[idx]
    duration = time.perf_counter_ns() - start
    print(f"prod: {duration}ns")
    
    start = time.perf_counter_ns()
    for _ in range(10000):
        ans = 0
        for i in range(3):
            for j in range(4):
                ans += ls[i][j]
    duration = time.perf_counter_ns() - start
    print(f"norm: {duration}ns")
    
    assert total == ans