def str_calc(s):
    if s == "":
        result = 0
    elif "," in s:
        nums = s.split(",")
        assert len(nums) in (2, 3)
        result = sum(map(to_num, nums))
    elif "\n" in s:
        lines = s.split("\n")
        if lines[0][:2] == "//":
            assert len(lines) == 2
            nums = lines[1].split(lines[0][2])
        else:
            nums = lines
        assert len(nums) in (2, 3)
        result = sum(map(to_num, nums))
    else:
        result = to_num(s)
    return result


def to_num(s):
    n = int(s)
    if n < 0:
        raise ValueError()
    return n if n <= 1000 else 0
