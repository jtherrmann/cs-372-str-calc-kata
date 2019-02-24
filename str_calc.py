def str_calc(s):
    if s == "":
        return 0
    nums = s.split(",")
    assert len(nums) in (1, 2)
    return sum(map(int, nums))
