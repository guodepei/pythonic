#!/bin/python3
# a one-page demo of pythonic programming

a, b = 1, 2
a, b = b, a # 1、变量交换

for i in range(6): # 2、循环遍历区间元素
    print(i)

colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors): # 3、带有索引位置的集合遍历
    print(i, '--->', color)

names = ['raymond', 'rachel', 'matthew', 'roger']
print(', '.join(names)) # 4、字符串连接

with open('README.md') as f: # 5、打开 / 关闭文件
    data = f.read()

print([i * 2 for i in range(10)]) # 6、列表推导式

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

@cache # 7、善用装饰器
def web_lookup(url):
    return urllib.urlopen(url).read()

from collections import deque # 8、合理使用列表
names = deque(['raymond', 'rachel', 'matthew', 'roger'])
names.popleft()
names.appendleft('mark')

p = 'vttalk', 'female', 30, 'python@qq.com'
name, gender, age, email = p # 9、序列解包

d = {"red":1, "blue":3, "green": 5}
for k, v in d.items(): # 10、遍历字典的
    print(k, '--->', v)