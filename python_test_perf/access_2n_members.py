import time
from itertools import product


def test(m):
    n = 2

    lst = [0] * n
    for _ in range(m):
        lst = [lst for _ in range(n)]

    print("dim:", m)

    cmdlist = ["    " * i + "for i" + str(i) + " in range(n):" for i in range(m)]
    cmdlist.append("    " * m + "_ = lst" + "".join("[i" + str(i) + "]" for i in range(m)))
    cmd = "\n".join(cmdlist)

    start = time.perf_counter()
    exec(cmd)
    old = time.perf_counter() - start
    print("old:", old)
    f.write(str(old))
    f.write(' ')

    it = product(range(n), repeat=m)
    cmd = "for i in it:\n" \
          "    _ = lst[i]"
    start = time.perf_counter()
    exec(cmd)
    new = time.perf_counter() - start
    print("new:", new)
    f.write(str(new))


f = open('access_2n_members.txt', 'w')
for m in range(1, 21):
    test(m)
    print()
    f.write('\n')
f.close()
