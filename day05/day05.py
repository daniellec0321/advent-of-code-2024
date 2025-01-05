import sys
from pprint import pprint



def puzzle1():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ans = 0
    graph = set()
    lines = data.split('\n')
    split_index = lines.index('')
    rules = lines[:split_index]
    updates = lines[split_index+1:]

    for rule in rules:
        page1, page2 = list(map(int, rule.strip().split('|')))
        graph.add((page1, page2))

    for update in updates:
        valid = True
        pages = list(map(int, update.strip().split(',')))
        for idx, p in enumerate(pages[:-1]):
            prev_pages = pages[:idx]
            next_pages = pages[idx+1:]
            for prev_page in prev_pages:
                if (p, prev_page) in graph:
                    valid = False
                    break
                if (prev_page, p) not in graph:
                    valid = False
                    break
            for next_page in next_pages:
                if (next_page, p) in graph:
                    valid = False
                    break
                if (p, next_page) not in graph:
                    valid = False
                    break
        if valid:
            mid_index = int(len(pages) / 2)
            ans += pages[mid_index]

    print(f'The answer to puzzle 1 is {ans}.')



def puzzle2():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ans = 0

    print(f'The answer to puzzle 2 is {ans}.')



if __name__ == '__main__':
    puzzle1()
    puzzle2()