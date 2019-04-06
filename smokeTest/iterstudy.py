'''迭代器'''
class Fibs:
    '''这是doc'''
    def __init__(self):
        print('init')
        self.a = 0
        self.b = 1
    def __next__(self):
        print('next')
        self.a,self.b = self.b, self.a+self.b
        return self.a
    def __iter__(self):
        print('iter')
        return self
