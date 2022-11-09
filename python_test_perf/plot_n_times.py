import matplotlib.pyplot as plt

dim = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
old = []
new = []
f = open('access_n_times.txt', 'r')
for line in f.readlines():
    o, n = map(float, line.split())
    old.append(o)
    new.append(n)
f.close()

plt.plot(dim, old, label="a[i][j]...")
plt.plot(dim, new, label="a[i, j, ...]")
plt.xscale("log")
plt.xlabel("n")
plt.yscale("log")
plt.ylabel("Time [s]")
plt.grid()
plt.legend()
plt.savefig('plot_n_times.png')
plt.show()
