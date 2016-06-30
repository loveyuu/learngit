# -*- coding: utf-8 -*-
"""
sudo apt-get update
sudo apt-get install libboost-python-dev
pip install multi_pattern_search
例子是github上自带的唯一比较烦人的是怎么安装
https://github.com/lanve/MultiPatternSearch.git
"""
from multi_pattern_search import MultiPatternSearch


search = MultiPatternSearch()

search.add_keyword("张沈鹏")
search.add_keyword("我是")

print search.exist("asdga sddqbq 珍珠饰张沈鹏品 ")
for k, v in search.count("我是张沈鹏.我是张沈鹏.我是张沈鹏.我是张沈 鹏.").iteritems():
    print k.decode('utf-8'), v
