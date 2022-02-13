import random

NUMBERS = 16


def load16(filename='16.txt'):
    names = []
    with open(filename, 'r', encoding='utf8') as f:
        for l in f.readlines():
            names.append(l.strip())

    if len(names) != NUMBERS:
        raise Exception('正赛选手应为{}名'.format(NUMBERS))
    return [names[0:4], names[4:8], names[8:12], names[12:]]


def rand16(filename='16.txt'):
    names = load16(filename)
    groups = ['A', 'B', 'C', 'D']
    ranks = [1, 2, 3, 4]
    with open('{}.md'.format(filename), 'w', encoding='utf8') as f:
        i = 0
        f.write('|group|name|\n')
        f.write('|---|---|\n')
        for rank in ranks:
            lst = names[i].copy()
            # group = groups.pop()
            # for no in range(len(lst)):
            for group in groups:
                name = lst.pop(random.randint(0, len(lst) - 1))
                info = '|{}{}|{}|'.format(group, rank, name)
                print(info)
                f.writelines('{}\n'.format(info))
            i += 1


if __name__ == '__main__':
    rand16('4/4th16.txt')

