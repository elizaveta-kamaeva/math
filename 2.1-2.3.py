def solver(a):
    r = 0
    for n in range(1, a + 1):
        r += 1 / n ** 2
    lim = (6 * r) ** 0.5
    print(lim)

while True:
    solver(int(input('N = ')))
