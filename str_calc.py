def str_calc(s):
    if s == "":
        result = 0
    elif "," in s:
        assert "\n" not in s
        nums = s.split(",")
        assert len(nums) in (2, 3)
        result = sum(map(to_num, nums))
    elif "\n" in s:
        assert "," not in s
        nums = s.split("\n")
        assert len(nums) in (2, 3)
        result = sum(map(to_num, nums))
    else:
        result = to_num(s)
    return result


def to_num(s):
    n = int(s)
    if n < 0:
        raise ValueError()
    return n
