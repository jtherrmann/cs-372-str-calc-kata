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
            delim = lines[0][2:]
            if len(delim) > 1:
                assert delim[0] == "[" and delim[-1] == "]"
                delim = delim[1:-1]
            nums = lines[1].split(delim)
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
