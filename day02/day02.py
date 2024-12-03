import sys



def puzzle1():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    safe_levels = 0

    for line in data.split('\n'):
        safe = True
        nums = list(map(int, line.strip().split()))
        increasing = nums[0] < nums[1]
        for idx, _ in enumerate((nums[:-1])):
            diff = abs(nums[idx] - nums[idx+1])
            if not (1 <= diff <= 3):
                safe = False
                break
            if increasing and (nums[idx] >= nums[idx+1]):
                safe = False
                break
            if not increasing and (nums[idx] <= nums[idx+1]):
                safe = False
                break
        if safe:
            safe_levels += 1

    print(f"The answer to puzzle 1 is {safe_levels}.")



def puzzle2():
    f = open(sys.argv[1])
    data = f.read()
    f.close()

    safe_levels = 0

    for line in data.split('\n'):
        safe = True
        nums = list(map(int, line.strip().split()))
        increasing = nums[0] < nums[1]
        for idx in range(0, len(nums)-1):
            diff = abs(nums[idx] - nums[idx+1])
            if not (1 <= diff <= 3):
                safe = False
                break
            if increasing and (nums[idx] >= nums[idx+1]):
                safe = False
                break
            if not increasing and (nums[idx] <= nums[idx+1]):
                safe = False
                break
        if safe:
            safe_levels += 1
            continue

        # If not safe, try removing a level
        for idx in range(0, len(nums)):
            new_nums = nums.copy()
            new_nums.pop(idx)
            safe = True
            increasing = new_nums[0] < new_nums[1]
            for idx in range(0, len(new_nums)-1):
                diff = abs(new_nums[idx] - new_nums[idx+1])
                if not (1 <= diff <= 3):
                    safe = False
                    break
                if increasing and (new_nums[idx] >= new_nums[idx+1]):
                    safe = False
                    break
                if not increasing and (new_nums[idx] <= new_nums[idx+1]):
                    safe = False
                    break
            if safe:
                safe_levels += 1
                break

    print(f"The answer to puzzle 2 is {safe_levels}.")



if __name__ == '__main__':
    puzzle1()
    puzzle2()