#!/bin/python3
# pythonic.py - a demo of python3 pythonic programming

'''A one file demo of python3 pythonic programming

For usage, try this:
$ python pythonic.py
'''

# 1、变量交换
a = 1
b = 2
a, b = b, a
print(a, b)

# 2、循环遍历区间元素
for i in range(6):
    print(i)

# 3、带有索引位置的集合遍历
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, '--->', color)

# 4、字符串连接
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
print(', '.join(names))

# 5、打开 / 关闭文件
with open('README.md') as f:
    data = f.read()
    print(data)

# 6、列表推导式
print([i * 2 for i in range(10)])

# 7、善用装饰器
import urllib.request as urllib # py3

def cache(func):
    saved = {}
    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page
    return wrapper

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

print(web_lookup("https://bing.com"))
print(web_lookup("https://bing.com"))

# 8、合理使用列表
from collections import deque
names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])
names.popleft()
names.appendleft('mark')
print(names)

# 9、序列解包
p = 'vttalk', 'female', 30, 'python@qq.com'
name, gender, age, email = p

# 10、遍历字典的
d = {"red":1, "blue":3, "green": 5}
for k, v in d.items():
    print(k, '--->', v)