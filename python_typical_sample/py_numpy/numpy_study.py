# encoding=utf-8
import numpy
from pprint import pprint


def study_list_unique():
    '''
    >>>[1, 5, 6, 2, 5, 6, 83, 8, 3, 3, 3, 7, 9]
    >>>(array([ 1,  2,  3,  5,  6,  7,  8,  9, 83]),
        array([ 0,  3,  8,  1,  2, 11,  7, 12,  6], dtype=int64))

        #nreturn_index 返回的index 是每个唯一的数第一次出现的位置
    '''
    l1 = [1, 5, 6, 2, 5, 6, 83, 8, 3, 3, 3, 7, 9]
    unique_l1 = numpy.unique(l1, return_index=True)
    pprint(l1)
    pprint(unique_l1)


def study_array_matrix():
    np_l1 = numpy.array([[5, 10, 15],
                         [20, 25, 30],
                         [35, 40, 45]])
    # sum all -> 225
    pprint(np_l1.sum())
    pprint(np_l1.max())
    pprint(np_l1.min())
    # average
    pprint(np_l1.mean())

    # sum column -> array([60, 75, 90])
    pprint(np_l1.sum(axis=0))
    # sum  line-> array([ 30,  75, 120])
    pprint(np_l1.sum(axis=1))

    # dot -> for array1 * array2
    # result array([[4, 1],[2, 2]])
    # 运算规则:
    # 1. 取出要计算元素相同的数据, 在第一个数组里取出此位置对应的行, 在第二个数组里取出此位置对应的列
    # 2. *行[0] * 列[0]) + (行[1] * 列[1]), .... -> 得出结果里的矩阵的[0][0]元素.
    a = [[1, 0], [0, 1]]
    b = [[4, 1], [2, 2]]
    pprint(numpy.dot(a, b))

    # array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81], dtype=int32)
    numpy.arange(10) ** 2

def main():
    study_list_unique()
    study_array_matrix()


main()
