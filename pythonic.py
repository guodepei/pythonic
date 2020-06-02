

# 1、变量交换
a, b = b, a

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
with open('data.txt') as f:
    data = f.read()

# 6、列表推导式
[i * 2 for i in range(10)]

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

def web_lookup(url):
    return cache(urllib.urlopen(url).read())

# 8、合理使用列表
from collections import deque
names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])
names.popleft()
names.appendleft('mark')

# 9、序列解包
p = 'vttalk', 'female', 30, 'python@qq.com'
name, gender, age, email = p

# 10、遍历字典的
for k, v in d.items():
    print(k, '--->', v)