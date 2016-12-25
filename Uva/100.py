import currenttime


def n3(n):
    times = 1
    while not n == 1:
        if not n % 2 == 0:
            n = 3 * n + 1
        else:
            n /= 2
        times += 1
        # print(n, end=' ')
    # print(times)
    return times


def maxn3(i, j):
    maxn = n3(i)
    for n in range(i, j+1):
        n3n = n3(n)
        if n3n > maxn:
            maxn = n3n
    return maxn


currenttime.showcurrenttime()
while(1):
    s = input()
    if not s.strip():
        break
    l = s.strip()
    i, j = l.split()
    print(i, j, maxn3(int(i), int(j)))
currenttime.showcurrenttime()