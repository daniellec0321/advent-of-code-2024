import sys



def puzzle1():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    l1 = list()
    l2 = list()

    for line in data.split('\n'):
        s = list(filter(lambda l: l != '', line.strip().split(' ')))
        l1.append(int(s[0]))
        l2.append(int(s[1]))

    l1 = sorted(l1)
    l2 = sorted(l2)
    diff = 0

    for n1, n2 in zip(l1, l2):
        diff += abs(n1 - n2)

    print(f'The answer to Day01 puzzle 1 is {diff}.')



def puzzle2():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    l1 = list()
    l2 = dict()

    for line in data.split('\n'):
        s = list(filter(lambda l: l != '', line.strip().split(' ')))
        l1.append(int(s[0]))
        num = int(s[1])
        l2[num] = l2.get(num, 0) + 1

    score = 0
    for num in l1:
        score += (num * l2.get(num, 0))

    print(f'The answer to puzzle 2 is {score}.')



if __name__ == '__main__':
    puzzle1()
    puzzle2()