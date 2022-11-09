import matplotlib.pyplot as plt

dim = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
old = []
new = []
f = open('access_2n_members.txt', 'r')
for line in f.readlines():
    o, n = map(float, line.split())
    old.append(o)
    new.append(n)
f.close()

plt.plot(dim, old, label="a[i][j]...")
plt.plot(dim, new, label="a[i, j, ...]")
plt.xticks(range(2, 21, 2))
plt.xlabel("n")
plt.yscale("log")
plt.ylabel("Time [s]")
plt.grid()
plt.legend()
plt.savefig('plot_2n_members.png')
plt.show()
