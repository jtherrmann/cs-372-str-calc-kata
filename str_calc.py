def str_calc(s):
    return sum(map(to_num, num_strs(s)))


def num_strs(s):
    s, delim = get_str_delim_pair(s)
    return s.replace(delim, " ").split()


def get_str_delim_pair(s):
    lines = s.split("\n")
    if lines[0][:2] == "//":
        delim = lines[0][2:]
        if len(delim) > 1:
            assert delim[0] == "[" and delim[-1] == "]"
            delim = delim[1:-1]
        s = "".join(lines[1:])
    else:
        delim = ","
    return s, delim


def to_num(s):
    n = int(s)
    if n < 0:
        raise ValueError()
    return n if n <= 1000 else 0
