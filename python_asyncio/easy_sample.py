import asyncio
from functools import partial
from time import sleep


def hello(*args, **kwargs):
    print('hello args:%s options:%s' % (args, kwargs))
    return args, kwargs


def stop_loop(loop):
    loop.stop()


loop = asyncio.get_event_loop()


def test1():
    '''all job start after loop.run_forever()
    this sample result:
    <TimerHandle when=20756.375 hello('xinxin521125')() at E:/Work/Python/FreamWork/scrapy_project/python_asyncio/easy_sample.py:5>
    hello xinx
    successful!

    even second register loop.call_later(1, partial(hello, 'xinxin521125'))
    still first to display.  be careful: it will not be real run currently.
    '''
    loop.call_soon(partial(hello, 'xinx', name='xinx'))
    x = loop.call_later(1, partial(hello, 'xinxin521125', name='xinxin521125'))
    print(x)
    # sleep(1)
    loop.call_soon(partial(stop_loop, loop))
    loop.run_forever()


def test1_1():
    '''call_soon callback receive func runable object not func result
    if not will receive [TypeError: 'tuple' object is not callable]
    '''
    loop.call_soon(hello('xinx'))
    loop.call_soon(partial(stop_loop, loop))
    loop.run_forever()


def test2():
    loop.call_later(1, partial(hello, 'test2'))
    loop.call_later(1, partial(stop_loop, loop))
    loop.run_forever()


def test_coordination():
    '''
    trivial args:(1, 2, 3, 4) options:{'name': 'trivial'}
    successful!
     '''

    @asyncio.coroutine
    def trivial(*args, **kwargs):
        print('trivial args:%s options:%s' % (args, kwargs))
        return args, kwargs

    loop.run_until_complete(trivial(1, 2, 3, 4, name='trivial'))


def test_run_background_loop():
    from threading import Thread

    def run_loop_forever(loop):
        def thread_1(loop, count, **kwargs):
            print('thread_1 job:%s, count:%s, options:%s' % (loop, count, kwargs))
            asyncio.set_event_loop(loop)
            loop.run_forever()

        thread = Thread(target=thread_1, args=(loop, 1), kwargs={'name': 'thread_test'})
        thread.start()
        return thread

    run_loop_forever(loop)
    loop.call_soon_threadsafe(partial(hello, 'background thread'))
    # loop.call_soon_threadsafe(partial(stop_loop, loop))


def teset_eventlet():
    '''
    define asyncio like eventlet. the func which have @asyncion.coroutine will return
    a generator object.
    internal logic for asyncio.coroutine's generator like below:
        try:
            next(generator)
        exception: StopIteration as error:
            return error.value  <- this is the generator func's return value
    :return:
    '''

    @asyncio.coroutine
    def sum_coroutine(*args):
        print('sum_coroutine args:%s ' % str(args))
        return sum(args)

    task = loop.run_until_complete(sum_coroutine(1, 2, 3, 4))
    print(task)
    print(sum_coroutine(1, 2, 3, 4))

    iter_obj = sum_coroutine(1, 2, 3, 4)
    try:
        next(iter_obj)
    except StopIteration as error:
        print('exception: %s' % error.value)


def test_yield_from():
    '''
    the func which have @asyncio.coroutine will return iter object.
    yield from also return iter object.
    '''

    @asyncio.coroutine
    def func_1(*args):
        print('func_1 args:%s ' % str(args))
        return [i for i in args]

    @asyncio.coroutine
    def func_2(*args):
        print('func_2 args:%s ' % str(args))
        result = yield from func_1(*[i * 2 for i in args])
        return result

    data = loop.run_until_complete(func_2(1, 2, 3, 4))
    print(data)


def test_task_1():
    '''
    future object is still in asyncio, it save the current loop object job's information.
    we can use this to make a distinction between all start task.

    task is the sub class of future
    one asyncio.coroutine have one task
    '''

    @asyncio.coroutine
    def func_3(*args):
        print('func_3 args:%s ' % str(args))
        loop.stop()
        return [i for i in args]

    task = asyncio.async(func_3(1, 2, 3, 4))
    print(task.done())
    # print(task.result())
    print("-" * 10)
    loop.run_forever()
    print(task.done())
    print(task.result())

    '''
    False
    ----------
    func_3 args:(1, 2, 3, 4) 
    True
    [1, 2, 3, 4]
    successful!
    '''


def test_async_callback():
    '''callback's arg have one parameter: furture, it saved the task run detail info.
    whether func_4 exception happen or success run, the call always run.
    callback's furture.result() can accept exception, when receive a exception will raise to task
    '''

    @asyncio.coroutine
    def func_4(*args, **kwargs):
        print('func_3 args:%s kwargs:%s' % (str(args), kwargs))
        # raise ValueError('xxxxxxx')
        return {'args': args, 'kwargs': kwargs}

    def func_cblk_1(furture, clbk_name, ):
        '''callback func is meaningless to return any thing.
          because none func can receive the callback return result'''
        print('func_calk args:', clbk_name, furture)
        print('furture dir:', dir(furture))
        # if main programe raise exception, furture.result() will raise the same exception
        print('run_result:', furture.result())
        # callback return any thine is meanless
        # return 'xxxxxxxxxxxxxx'

    def func_cblk_2(arg1, furture):
        '''
        callback with args style of writing.
            arg must write to frist ex: def callbck(arg1, arg2,...,, furture)
        callback with kwargs style of writing:
            kwargs must write after furture ex: def callback(furture, **kwargs)

        'furture' is the default task's information, it call save the every task run detail.

        '''
        print('func_cblk args:', arg1, furture)
        print('run_result:', furture.result())

    task = asyncio.async(func_4(1, 2, 3, name='callback'))
    # task can register multi callback func
    task.add_done_callback(partial(func_cblk_1, clbk_name='****haha,good****'))
    task.add_done_callback(partial(func_cblk_2, '****arg1,good****'))
    loop.run_until_complete(task)

    print('task result: %s' % task.result())


def test_multi_tasks():
    '''we can add a callback for a group multi task job'''

    @asyncio.coroutine
    def task_1(*args, **kwargs):
        print('task_1 args:%s kwargs:%s' % (str(args), kwargs))
        if not (args and kwargs):
            sleep(1)
        return {'args': args, 'kwargs': kwargs}

    def cblk(furture, success_flg):
        print('cblk func', success_flg)
        print(furture.result())

    multi_task = asyncio.gather(
        task_1(1, 2, 3),
        task_1(name='gather'),
        task_1(1, 2, 4, run_sum='get total'),
        task_1(),
    )
    multi_task.add_done_callback(partial(cblk, success_flg=True))
    results = loop.run_until_complete(multi_task)
    print('--------')
    print(results)
    for _result in results:
        print(_result)
        if _result.get('kwargs') == {}:
            print('failed')
            break
    print('--------')


def test_wait_task():
    @asyncio.coroutine
    def task_1(*args, **kwargs):
        print('task_1 args:%s kwargs:%s' % (str(args), kwargs))
        wait_time = kwargs.get('wait', 0)
        print('sleep: %s' % wait_time)
        # asyncio.sleep(wait_time)
        sleep(wait_time)
        return {'args': args, 'kwargs': kwargs}

    @asyncio.coroutine
    def task_2(*args, **kwargs):
        print('task_1 args:%s kwargs:%s' % (str(args), kwargs))
        wait_time = kwargs.get('wait', 0)
        print('sleep: %s' % wait_time)
        # asyncio.sleep(wait_time)
        sleep(wait_time)
        return {'args': args, 'kwargs': kwargs}

    def cblk(furture):
        print('cblk')
        print(furture.result())

    multi_task = asyncio.wait(
        [
            task_1(1, wait=1, name='1'),
            task_1(2, wait=2, name='2'),
            task_2(3, wait=3, name='3'),
            task_2(4, wait=4, name='4'),
        ],
        timeout=1,
        return_when=asyncio.FIRST_COMPLETED,
        # return_when=asyncio.FIRST_EXCEPTION,
    )
    # multi_task.add_done_callback(cblk)
    result = loop.run_until_complete(multi_task)
    print(result)


test_wait_task()

print('successful!')
