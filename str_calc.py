def str_calc(s):
    if s == "":
        result = 0
    elif "," in s:
        assert "\n" not in s
        nums = s.split(",")
        assert len(nums) == 2
        result = sum(map(int, nums))
    elif "\n" in s:
        assert "," not in s
        nums = s.split("\n")
        assert len(nums) == 2
        result = sum(map(int, nums))
    else:
        result = int(s)
    return result
