import time


def test(m, f):
    n = 1000

    lst = [0]
    for _ in range(m):
        lst = [lst for _ in range(n)]

    print("dim:", m)

    cmd = "for i in range(n):\n" \
          "    _ = lst" + "[0]" * m
    start = time.perf_counter()
    exec(cmd)
    old = time.perf_counter() - start
    print("old:", old)
    f.write(str(old))
    f.write(' ')

    cmd = "for i in range(n):\n" \
          "    _ = lst[" + str((0, ) * m) + "]"
    start = time.perf_counter()
    exec(cmd)
    new = time.perf_counter() - start
    print("new:", new)
    f.write(str(new))


f = open('access_n_times.txt', 'w')
for m in [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]:
    test(m, f)
    print()
    f.write('\n')
f.close()
