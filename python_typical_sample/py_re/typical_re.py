import re
from pprint import pprint


def test_1():
    sample_str = "This is hello world sample. is this a apple."

    # find from start
    pprint(re.match('is', sample_str))
    # find anywhere
    pprint(re.search('is', sample_str))
    # find all
    pprint(re.findall('is', sample_str))

    # 匹配捕获组
    m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    pprint(m.group(0))
    pprint(m.group(1))
    pprint(m.group(2))

def main():
    test_1()


main()
