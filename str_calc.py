def str_calc(s):
    if s == "":
        result = 0
    elif "," not in s:
        result = int(s)
    else:
        nums = s.split(",")
        assert len(nums) == 2
        result = sum(map(int, nums))
    return result
