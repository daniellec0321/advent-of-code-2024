import sys
import re



def puzzle1():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ans = 0
    search_string = r"mul\(\d{1,3},\d{1,3}\)"
    results = re.findall(search_string, data)
    for res in results:
        num1, num2 = map(int, res[4:-1].split(','))
        ans += (num1 * num2)

    print(f'The answer to puzzle 1 is {ans}.')



def puzzle2():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ans = 0
    do_search_string = r"do\(\)"
    dont_search_string = r"don't\(\)"
    mul_search_string = r"mul\(\d{1,3},\d{1,3}\)"
    
    enabled = True
    while data:
        if enabled:
            match = re.search(dont_search_string, data)
            if not match:
                to_search = data
                data = ''
            else:
                to_search = data[:match.start()]
                data = data[match.end():]
            results = re.findall(mul_search_string, to_search)
            for res in results:
                num1, num2 = map(int, res[4:-1].split(','))
                ans += (num1 * num2)
        else:
            match = re.search(do_search_string, data)
            if not match:
                data = ''
            else:
                data = data[match.end():]
        enabled = not enabled

    print(f'The answer to puzzle 2 is {ans}.')



if __name__ == '__main__':
    puzzle1()
    puzzle2()