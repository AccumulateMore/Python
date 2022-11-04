# with语句可以自动管理上下文资源，不管什么原因跳出with块，都能确保文件正常关闭，以此来达到释放资源的目的
print(type(open('a.txt', 'r')))  # 上下文管理器
with open('a.txt', 'r') as file:
    print(file.read())  # 离开with语句自动释放，不用close()

"""
MyContentMgr实现了特殊方法enter和exit称为该类对象遵守了上下文管理器协议
该诶对象的实例对象称为上下文管理器
MyContentMgr()为实例对象
"""


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法调用执行了')

    def show(self):
        print('show方法调用执行了', 1/0)


with MyContentMgr() as file:  # 相当于file=MyContentMgr()
    file.show()  # 产生异常也调用了exit方法
