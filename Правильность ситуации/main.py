with open('input.txt') as f:
    inp = []
    for line in f:
        inp.append(line.strip())


def win(l, a):
    if l[0] == l[1] == l[2] == a or l[3] == l[4] == l[5] == a or l[6] == l[7] == l[8] == a:
        return True
    if l[0] == l[3] == l[6] == a or l[1] == l[4] == l[7] == a or l[2] == l[5] == l[8] == a:
        return True
    if l[0] == l[4] == l[8] == a or l[2] == l[4] == l[6] == a:
        return True
    return False


def pos(lines):
    n1 = lines.count('1')
    n2 = lines.count('2')
    if n1 - n2 < 2 and n1 >= n2:
        if not (win(lines, '1') and win(lines, '2')):
            if not (win(lines, '2') and n1 != n2):
                if not (win(lines, '1') and n1 - n2 != 1):
                    return 'YES'
    return 'NO'


lines = (inp[0] + inp[1] + inp[2]).replace(' ', '')
print(pos(lines))
