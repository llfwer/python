# http://python.jobbole.com/83610/


def generator():
    my_list = range(10)
    for i in my_list:
        yield i * i


# yield是一个关键词，类似return, 不同之处在于，yield返回的是一个生成器
g = generator()
# g is an object!
print(g)

for m in g:
    print(m)

'''
    第一次函数将会从头运行，直到遇到yield，然后将返回循环的首个值. 
    然后，每次调用，都会执行函数中的循环一次，返回下一个值，直到没有值可以返回
    当循环结束，或者不满足”if/else”条件，导致函数运行但不命中yield关键字，此时生成器被认为是空的
'''
