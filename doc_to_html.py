class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
# class FooChild(FooParent):
#     def __init__(self):
#         FooParent.__init__(self)
#         print('Child')
#
#     def bar(self, message):
#         # FooParent.bar(self, message)
#         super().bar(message)
#         # print(FooParent.bar())
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')

def deco_1(func):
    print("into deco1")
    def wrapper(a, b):
        print("enter into deco1 wrapper")
        # a += 1
        # b += 1
        func(a,b)
        print("over deco1")
    return wrapper


def deco_2(func):
    print("into deco2")
    def wrapper(a, b):
        print("enter into deco2 wrapper")
        # a += 1
        # b += 1
        func(a, b)
        print("over deco2")
    return wrapper

# @deco_1
# @deco_2
# def addfunc(a, b):
#     print(f"add res{a + b}")

# deco_2(addfunc)
# addfunc(3,4)
# b = deco_1(deco_2(addfunc))(3,4)


# len_num = 5*12
# dic = {"A": 10, "B": 7, "C": 5, "D": 4}
# for num in range(len_num):
#     max_key = max(dic, key=dic.get)
#     dic[max_key] -= 3
#     for k in list(dic.keys()):
#         if k != max_key:
#             dic[k] += 1
# print('结果', dic)
# print(isinstance(dic, dict))



def new_sid_by_type(sid, sid_type: int):
    if sid_type == 0:
        return str(int(sid) + 1)
    # 标题共九级
    num = (9-sid_type)
    # 4位正文id
    title_sid = int(sid[: -(4+num*3)])
    new_sid = str(title_sid + 1) + '000'*num + '0000'
    return new_sid

NINE_TYPE = 9
TEXT_LENGTH = 4
TITLE_LENGTH = 3
def get_title_sid(sid, sid_type):
    # 标题共九级
    num = (int(NINE_TYPE) - sid_type)
    print(num)
    # 4位正文id
    title_sid = sid[: -(TEXT_LENGTH + num * TITLE_LENGTH)]
    print(title_sid, TEXT_LENGTH + num * TITLE_LENGTH)
    return title_sid
s = '10010020010000000000000000000000'
# sid_type = 4
get_title_sid(s, 3)
