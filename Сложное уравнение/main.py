with open('input.txt') as f:
    a, b, c, d = list(map(int, f.readlines()))


def f(a, b, c, d):
    if a != 0 or a and b != 0:
        x = -b / a
        if c * x + d != 0:
            if str(x).split('.')[1] == '0':
                return int(x)
        return 'NO'
    return 'INF'


print(f(a, b, c, d))
