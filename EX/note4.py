# Python高级编程技巧实战
# 2018/04/15

"""----------------------------"""

# 如何拆分含有多種分割符的字符串

# 空白
s = 'aaa bb cccc   dd eeee  688'
s.split()


# 多種
s = 'aaa ;dd eeee  /ffff; jjjj\ 123 4  5    688'
res = s.split(';')

# ['aaa ', 'dd eeee  /ffff', ' jjjj\\ 123 4  5    688']

res = map(lambda x: x.split('\\'),res)

# [['aaa '], ['dd eeee  /ffff'], [' jjjj', ' 123 4  5    688']]

t = []

res = map(lambda x: t.extend(x.split('/')),res)

#[None, None, None]

# t = ['aaa ', 'dd eeee  ', 'ffff', ' jjjj\\ 123 4  5    688']

res = t

t = []

map(lambda x: t.extend(x.split(',')),res)
#[None, None, None]

def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        list(map(lambda x: t.extend(x.split(d)),res))
        res = t
    # 過濾空字符 
    return [x for x in res if x]

s = 'aaa;dd,eeeffff;jjjj123,4;688'
print(mySplit(s,';,'))



--------------
import re

s = 'aaa;dd,ee/efff/f;jjjj123,4;688'

print(re.split('[,;/]+',s))

#['aaa', 'dd', 'ee', 'efff', 'f', 'jjjj123', '4', '688']


"""----------------------------"""

# 如何調整字符串中文本的格式

# 將yyyy-mm-dd => mm/dd/yyyy

import re

s = '2018-03-16'



#使用正則表達是re.sub

a = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',s)
# '03/16/2018'


c = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',s)
# 可以幫每個組取名子

"""----------------------------"""

# 如何將小字符串拼成大字符串


p1 = ["<0112>","<32>","<1024*768>","<60>","<1>","<100.0>","<500.0>",]

s = ''

for p in p1:
    s += p



''.join(p1)

# '<0112><32><1024*768><60><1><100.0><500.0>'

l = ['abc',123,45,'xyz']

''.join([str(x) for x in l ])

#生成器表達式 比列表解析小

''.join(str(x) for x in l )
# 'abc12345xyz'

"""----------------------------"""
# 如何將字符串進行左右居中對齊

s = 'abc'

s.ljust(20)
						     
# 'abc                 '
s.ljust(20,'=')
						     
# 'abc================='
s.rjust(20)
						     
# '                 abc'
s.rjust(20,'=')

# '=================abc'

s.center(20)
						     
# '        abc         '
s.center(20,'=')
						     
# '========abc========='

format(s,'<20')
						     
#'abc                 '
format(s,'>20') 
						     
# '                 abc'
format(s,'^20')
						     
# '        abc         '

d = {
    "lodDist":100.0,
    "SmallCull":0.04,
    "DistCull":500.0,
    "trilinear":40,
    "farclip":477,
    }



d.keys()
# ['lodDist', 'SmallCull', 'DistCull', 'trilinear', 'farclip']

list(map(len,d.keys()))
# [7, 9, 8, 9, 7] 看哪個最長
w = max(list(map(len,d.keys())))
# 9

for k in d:
    print(k.ljust(w), ':',d[k])
'''
lodDist   : 100.0
SmallCull : 0.04
DistCull  : 500.0
trilinear : 40
farclip   : 477
'''

"""----------------------------"""
# 如何去掉字符串中不需要的字符

s = '   abc   123   '

s.strip()
						     
# 'abc   123'
s.lstrip()
						     
# 'abc   123   '
s.rstrip()
						     
# '   abc   123'

s = '---abc+++'

s.strip('-+')
						      
# 'abc'

s = 'abc:123'
			     
s[:3]+s[4:]
						     
# 'abc123'

s = '\tabc\t123\txyz'
						     
s.replace('\t','')
						     
# 'abc123xyz'


s = '\tabc\t123\txyz\ropq\r'
						     
import re
						     
re.sub('[\t\r]','',s)
						     
# 'abc123xyzopq'

s = 'abc1230323xyz'
						     
#文本加密a-x b-y c-z 互換
						     
str.maketrans('abcxyz','xyzabc')
						     
# {97: 120, 98: 121, 99: 122, 120: 97, 121: 98, 122: 99}

s.translate(str.maketrans('abcxyz','xyzabc'))
						     
# 'xyz1230323abc'

s = 'hànyǔ pīnyīn'
# 移掉音標

        
