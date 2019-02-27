# conding=utf-8
import types


class Person(object):
    str = ' '
    info = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setInfo(self, info):
        self.info = info

    def print(self):
        print("我的名字是%s，我%d岁了" % (self.name, self.age))

    def strJoin(self, str):
        print(self.str.join(str))
        print(self.str)
        print(str)

    def isspace(self, str):
        if str == None:
            print(True)
        elif str.isspace():
            print(True)
        else:
            print(False)

    def isTrue(self, s):
        if (s):
            print(True)
        else:
            print(False)

    def viewTuble(self, tu, index):
        return tu[index]

    def getParmFInfo(self, parm):
        return self.info.get(parm,"没有查到你想要的信息")


def run(cls, spleed):
    print("我叫%s，我在奔跑，我的速度是%dkm/h" % (cls.name, spleed))


p = Person("xiaohua", 10)
p.print()
p.run = types.MethodType(run, p)
p.run(100)
try:
    p.run()
except:
    print("刚刚发生什么了 ，我在哪里，我是谁！")
else:
    print("haha ! what can i do!")
# p.strJoin("2121")

# print("wqwq".join("--"))
# p.isspace(" ")
p.isTrue(' ')
a = ()
p.isTrue(a)
print(p.viewTuble((1, 2, 3, 4), 3))
a={"name": "wqwq", "age": 12}
p.setInfo(a)
print(p.getParmFInfo('age1'))
print(len(a))
print(a.keys())
print(a.values())
print('sasa')