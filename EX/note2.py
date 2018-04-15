# Python高级编程技巧实战
# 2018/04/15

"""----------------------------"""
# 計算數字出現次數
from random import randint
from collections import Counter

data = [randint(0,20) for i in range(30)]

print(data)
c = dict.fromkeys(data,0)
print(c)

for x in data:
    c[x] += 1
print(c)

c2 = Counter(data)

#出現次數前三名
c2.most_common(3)

print(c2)


"""----------------------------"""
# 計算單字出現次數
import re
from collections import Counter

txt = open('alice.txt').read()

c3 = Counter(re.split('\W+',txt))
#Counter({'dat': 8, 'alice': 5, 'bob': 3, 'cccc': 3, 'seeeio': 2, 'ikojk': 1})

c3.most_common(2)

#[('dat', 8), ('alice', 5)]

"""----------------------------"""
# 使用字典值排序

from random import randint

c = {x:randint(60,100) for x in 'abcdefg'}
#{'a': 96, 'b': 65, 'c': 98, 'd': 94, 'e': 78, 'f': 65, 'g': 63}

sorted(c)
#['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 1.
# 使用元組來比較
# (98,'c') (96,'a')


# 使用zip來讓字典變元組


d = zip(c.values(),c.keys())
# [(96, 'a'), (65, 'b'), (98, 'c'), (94, 'd'), (78, 'e'), (65, 'f'), (63, 'g')]

sorted(d)
# [(63, 'g'), (65, 'b'), (65, 'f'), (78, 'e'), (94, 'd'), (96, 'a'), (98, 'c')]

# 2.
c.items()
# ([('a', 96), ('b', 65), ('c', 98), ('d', 94), ('e', 78), ('f', 65), ('g', 63)])

sorted(c.items(),key=lambda x:x[1])
# [('g', 63), ('b', 65), ('f', 65), ('e', 78), ('d', 94), ('a', 96), ('c', 98)]


"""----------------------------"""

# 如何找到多個字典的公共鍵

from random import randint,sample

# 隨機產生各個字典的鍵
sample('abcdefg',randint(3,6))

s1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
# {'a': 1, 'g': 2, 'f': 2}

s2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
# {'g': 3, 'f': 3, 'b': 4, 'a': 1}

s3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
# {'a': 1, 'd': 4, 'f': 3, 'e': 4, 'c': 2}

# 1
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

res
#['a', 'f']

#2
s1.keys()
#dict_keys(['a', 'g', 'f'])

s2.keys()
#dict_keys(['g', 'f', 'b', 'a'])

s3.keys()
#dict_keys(['a', 'd', 'f', 'e', 'c'])

#使用集合
s1.keys() & s3.keys() & s2.keys()
#{'f', 'a'}

#3
import functools
map(dict.keys,[s1,s2,s3])
#[dict_keys(['a', 'g', 'f']), dict_keys(['g', 'f', 'b', 'a']), dict_keys(['a', 'd', 'f', 'e', 'c'])]

functools.reduce(lambda a,b:a&b,map(dict.keys,[s1,s2,s3]))
#{'f', 'a'}

"""----------------------------"""
# 如何讓字典維持有序
# python 3.6 開始有序
d = {}
d['Jim'] = (1,35)
d['Leo'] = (2,37)
d['Bob'] = (3,40)
for k in d:
    print(k)

from collections import OrderedDict

d = OrderedDict()
d['Jim'] = (1,35)
d['Leo'] = (2,37)
d['Bob'] = (3,40)

for k in d:
    print(k)
	
"""----------------------------"""

# 如何讓字典維持有序
# python 3.6 開始有序
from time import time
from random import randint
from collections import OrderedDict

d = OrderedDict()

players = list("ABCDEFGH")
start = time()

for i in range(8):
    input()
    # 每次隨機選擇一名打擊完畢
    p = players.pop(randint(0,7-i))
    end = time()
    print(i+1,p,end-start)
    d[p] = (i+1,end-start)

print('-'*20)

for k in d:
    print(k,d[k])

"""----------------------------"""
1 A 3.5332021713256836

2 E 4.124236106872559

3 B 4.50025749206543

4 G 4.868278503417969

5 H 5.132293701171875

6 F 5.332305192947388

7 D 5.571318864822388

8 C 5.915338516235352
--------------------
A (1, 3.5332021713256836)
E (2, 4.124236106872559)
B (3, 4.50025749206543)
G (4, 4.868278503417969)
H (5, 5.132293701171875)
F (6, 5.332305192947388)
D (7, 5.571318864822388)
C (8, 5.915338516235352)


"""----------------------------"""
# 實現歷史紀錄功能

from random import randint
from collections import deque
from io import StringIO

import pickle

# 只有5個得隊列
history = deque([],5)

N = randint(0,100)
#pickle.loads()

def guess(k):
    if k == N:
        print('right')
        return True
    elif k < N:
        print('%s if less than N' %k)
    else:
        print('%s if greater than N' %k)
    return False

    

while True:
    line = input('please input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))

history = str(history)
pickle.dump(history,open('alice','wb'))
 



