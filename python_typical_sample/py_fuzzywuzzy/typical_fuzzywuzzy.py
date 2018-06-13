# encoding=utf-8
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from pprint import pprint


def test1():
    # 完全比对
    # >>> 'ratio_1: 82'
    ratio_1 = fuzz.ratio("this is a test", "Wow! this is a test!")
    pprint('ratio_1: {}'.format(ratio_1))

    # 部分比对
    # >>> 'ratio_2: 100'
    ratio_2 = fuzz.partial_ratio("this is a test", "Wow! this is a test!")
    pprint('ratio_2: {}'.format(ratio_2))

    # 排序后比对
    # full_process 默认是True  可以去除标点符号
    # >>> 'ratio_sort_tmp: 83'
    # >>> 'ratio_sort: 100'
    # >>> 'ratio_sort_not_full_prcess: 63'
    ratio_sort_tmp = fuzz.ratio('this is a test', 'is this a test?')
    ratio_sort = fuzz.token_sort_ratio('@#this is a test!', '#@#is this a test?')
    ratio_sort_not_full_prcess = fuzz.token_sort_ratio('@#this is a test!', '#@#is this a test?', full_process=False)
    pprint('ratio_sort_tmp: {}'.format(ratio_sort_tmp))
    pprint('ratio_sort: {}'.format(ratio_sort))
    pprint('ratio_sort_not_full_prcess: {}'.format(ratio_sort_not_full_prcess))

    # 筛出集合中唯一元素,在比较
    # 'ratio_set_tmp: 61'
    # 'ratio_set: 100'
    ratio_set_tmp = fuzz.ratio('this is a test', 'is this a, test, is this a test?')
    ratio_set = fuzz.token_set_ratio('this is a test', 'is this a, test, is this a test?')
    pprint('ratio_set_tmp: {}'.format(ratio_set_tmp))
    pprint('ratio_set: {}'.format(ratio_set))

    # 在集合中选取近似项目
    # >>> ("src_list: ['Atlanta Falcons', 'New York Jets', 'New York Giants', 'Dallas Cowboys']")
    # >>> "choices: [('New York Jets', 90), ('New York Giants', 90)]"
    # >>> "choice_one: ('New York Jets', 90)"
    src_list = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
    choices = process.extract(query='new york', choices=src_list, limit=2)
    choice_one = process.extractOne('new york', src_list)
    pprint('src_list: {}'.format(src_list))
    pprint('choices: {}'.format(choices))
    pprint('choice_one: {}'.format(choice_one))

    # processor default is fuzz.utils.full_process (即将字符串变为小写，
    #        去掉除字母和数字之外的字符（发现不能去掉-字符），剩下的字符串以空格分开)
    # scorer default is fuzz.WRatio (计算两个字符串相似度的函数)
    # >>> "process_extra: [('New York Jets', 90)]"
    process_extra = process.extract(query='new york', choices=src_list,
                                    processor=fuzz.utils.full_process, limit=1, scorer=fuzz.WRatio)
    pprint('process_extra: {}'.format(process_extra))

    # 当score小于该阈值时，不会输出。返回一个生成器，输出每个大于
    # score_cutoff的匹配，按顺序输出，不排序。
    # >>> 'process_noorder: <generator object extractWithoutOrder at 0x0000017417371620>'
    # >>> "process_noorder: [('New York Jets', 90), ('New York Giants', 90)]"
    process_noorder = process.extractWithoutOrder(query='new york',
                                                  choices=src_list,
                                                  processor=fuzz.utils.full_process,
                                                  scorer=fuzz.WRatio, score_cutoff=50)
    pprint('process_noorder: {}'.format(process_noorder))
    pprint('process_noorder: {}'.format(list(process_noorder)))

    # process.extractBests（）和process.extract（）都调用了process.extractWithoutOrder（），
    # 只不过process.extractBests（）能传输 score_cutoff。
    # >>> "process_best: [('New York Jets', 90), ('New York Giants', 90)]"
    process_best = process.extractBests(query='new york', choices=src_list,
                                        processor=fuzz.utils.full_process,
                                        scorer=fuzz.WRatio,
                                        score_cutoff=90, limit=5)
    pprint('process_best: {}'.format(list(process_best)))

    # 也调用了process.extractWithoutOrder（），只不过输出一个score最高的值。
    # >>> "process_best_one: ['New York Jets', 90]"
    process_best_one = process.extractOne(query='new york', choices=src_list,
                                          processor=fuzz.utils.full_process,
                                          scorer=fuzz.WRatio,
                                          score_cutoff=90)
    pprint('process_best_one: {}'.format(list(process_best_one)))

    # 取相似度最小和最大的项目
    # contains_dupes是数组，元素为字符串。
    # 取出相似度小于 threshold的字符串，相似度大于 threshold的字符串取最长一个
    # >>. "process_worst: ['Atlanta Falcons', 'New York Giants']"
    process_worst = process.dedupe(contains_dupes=src_list, threshold=20, scorer=fuzz.token_set_ratio)
    pprint('process_worst: {}'.format(list(process_worst)))


def main():
    test1()


main()
