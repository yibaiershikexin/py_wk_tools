def test_without_format():
    _str = "Sample string: %s, List item:%s, integer:%4d, float: %.2f"
    _list = ['str' + str(i) for i in range(5)]
    _int = 10
    _float = 10.12345678
    param = ('hello world', _list, _int, _float)

    # fill space to integer
    # >Sample string: hello world, List item:['str0', 'str1', 'str2', 'str3', 'str4'], integer:  10, float: 10.12
    print_str = _str % param
    print(print_str)

    # fill 0 to integer [integer:%04d,]
    # >Sample string: hello world, List item:['str0', 'str1', 'str2', 'str3', 'str4'], integer:0010, float: 10.12
    _str1 = "Sample string: %s, List item:%s, integer:%04d, float: %.2f"
    print_str1 = _str1 % param
    print(print_str1)


def test_use_format():
    _str = "Sample string: {}, List item:{}, integer:{}, float:{}"
    params_dict = {
        'str_': 'hello world',
        '_int': 100000,
        '_float': 10.12345678,
        '_list': ['str' + str(i) for i in range(5)],
    }
    params_tuple = (params_dict['str_'],
                    params_dict['_list'],
                    params_dict['_int'],
                    params_dict['_float'])
    # > Sample string: hello world, List item:['str0', 'str1', 'str2', 'str3', 'str4'], integer:100000, float:10.12345678
    print(_str.format(params_tuple[0], params_tuple[1], params_tuple[2], params_tuple[3]))
    print(_str.format(*params_tuple))

    # specify index
    # > Sample string: hello world, List item:str2, integer:100000, float:10.12345678
    _str1 = "Sample string: {}, List item:{[2]}, integer:{}, float:{}"
    print(_str1.format(*params_tuple))

    # param dict
    # > Sample string: hello world, List item:['str0', 'str1', 'str2', 'str3', 'str4'], integer:100000, float:10.12345678
    _str2 = "Sample string: {str_}, List item:{_list}, integer:{_int}, float:{_float}"
    print(_str2.format(**params_dict))

    # float
    # > Sample string: hello world, List item:['str0', 'str1', 'str2', 'str3', 'str4'], integer:100000, float:10.1235
    _str2_1 = "Sample string: {str_}, List item:{_list}, integer:{_int}, float:{_float:.4f}"
    print(_str2_1.format(**params_dict))

    # int
    # > Sample string: hello world, List item:['str0', 'str1', 'str2', 'str3', 'str4'], integer:100,000, float:10.12345678
    _str2_2 = "Sample string: {str_}, List item:{_list}, integer:{_int:,}, float:{_float}"
    print(_str2_2.format(**params_dict))


def main():
    test_without_format()
    test_use_format()

main()
