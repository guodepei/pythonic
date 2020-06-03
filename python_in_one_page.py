#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-- 数字常量
    0x9ff, 0X9FF, 0b101010                       # 十六进制、二进制数字
    int(string, base)                            # 将字符串转化为整数，base为进制数

#-- 数字的表达式操作符
    x if y else z                                # 三元选择表达式
    1 < a < 3                                    # Python中允许连续比较
    x[i], x[i:j:k]                               # 索引、分片、调用

#-- 集合set
    s = set([3,5,9,10])                          # 创建一个数值集合，返回{3, 5, 9, 10}
    {x**2 for x in [1, 2, 3, 4]}                 # 集合解析，结果：{16, 1, 4, 9}

#-- 字符串
    S[1:3], S[1:], S[:-1], S[1:10:2]             # 分片，第三个参数指定步长，如`S[1:10:2]`是从1位到10位没隔2位获取一个字符。
    int('42'), str(42)                           # 返回(42, '42')
    "%d...%6d...%-6d...%06d" % (1234, 1234, 1234, 1234)         # 对齐方式及填充："1234...  1234...1234  ...001234"
    "%(name1)d---%(name2)s" % {"name1":23, "name2":"value2"}    # 基于字典的格式化表达式
    "{motto} and {0}".format('ham', motto = 'spam')             # 混合调用
    "{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)   # 输出'3.141590e+00, 3.142e+00, 3.14159'

#-- 常用列表常量和操作
    L = [[1, 2], 'string', {}]                    # 嵌套列表
    L = list(range(0, 4))                         # 列表初始化    
    a = [], a += [1]                              # 这里实在原有列表的基础上进行操作，即列表的id没有改变
    del a[::2]                                    # 去除偶数项(偶数索引的)，a = [1, 3, 5, 7]

#-- 常用字典常量和操作
    D = {'spam':2, 'tol':{'ham':1}}               # 嵌套字典  
    D = dict([('name', 'tom'), ('age', 12)])      # {'age': 12, 'name': 'tom'}
    del D['key']                                  # 删除字典的某一项

#-- 元组和列表的唯一区别在于元组是不可变对象，列表是可变对象
    a = (1, 2, 3)                                 # a[1] = 0, Error

#-- 列表解析语法
    for teama, teamb in zip(["Packers", "49ers"], ["Ravens", "Patriots"]): # 两个列表同时解析：使用zip函数
    for index, team in enumerate(["Packers", "49ers", "Ravens", "Patriots"]): # 输出0, Packers \n 1, 49ers \n ......

#-- 生成器表达式
    G = (sum(row) for row in M)                   # 使用小括号可以创建所需结果的生成器generator object
    next(G), next(G), next(G)                     # 输出(6, 15, 24)