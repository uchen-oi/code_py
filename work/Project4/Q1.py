from functools import wraps
from time import strftime


def deco(log_file):
    def outer(func):
        @wraps(func)
        def inner(*args,**kwargs):
            with open(log_file,'a+') as f:
                f.write(f'函数名称：{func.__name__},调用时间：{strftime('%H:%M:%S')}')
            return func
        return inner
    return outer
@deco('/log1.txt')
def fun1():
    print('fun1被调用')

if __name__=='__main__':
    fun1()