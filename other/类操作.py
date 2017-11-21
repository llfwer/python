'''
program: 类操作
version: python 3.5.3
time: 2017/11/14
author: rowe
'''


class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def get_age(self):
        return self.age


obj = Test('rowe', 31)
obj.show_name()
print('Age is ' + str(obj.get_age()))
