# encoding=utf-8
data = {'name': 'linbin', 'age': 24, 'sexy': 'male'}


def handle_1(name=None, age=0, sexy=None):
    print name, age, sexy

handle_1(**data)  # 解包(unpacking)


def handle_2(**kwargs):  # 装包(packing)
    print kwargs

handle_2(area='Shanghai', street='TangQiao', door_num=1402)
# 有时候不经意间会发现以前经常忽略和不重视的东西
