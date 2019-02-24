def str_calc(inpt):
    return sum(map(to_num, num_strs(inpt)))


def to_num(num_str):
    num = int(num_str)
    if num < 0:
        raise ValueError()
    return num if num <= 1000 else 0


def num_strs(inpt):
    delim, rest = extract_delim(inpt)
    return rest.replace(delim, " ").split()


def extract_delim(inpt):
    lines = inpt.split("\n")
    if lines[0][:2] == "//":
        return parse_delim(lines[0][2:]), "".join(lines[1:])
    return ",", inpt


def parse_delim(delim):
    return parse_multi_char_delim(delim) if len(delim) > 1 else delim


def parse_multi_char_delim(delim):
    assert delim[0] == "[" and delim[-1] == "]"
    return delim[1:-1]
