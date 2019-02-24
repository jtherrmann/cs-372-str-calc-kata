def str_calc(s):
    lines = s.split("\n")
    if lines[0][:2] == "//":
        delim = lines[0][2:]
        if len(delim) > 1:
            assert delim[0] == "[" and delim[-1] == "]"
            delim = delim[1:-1]
        s = "".join(lines[1:])
    else:
        delim = ","

    nums = s.replace(delim, " ").split()
    return sum(map(to_num, nums))


def to_num(s):
    n = int(s)
    if n < 0:
        raise ValueError()
    return n if n <= 1000 else 0
