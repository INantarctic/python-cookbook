# Python高级编程技巧实战
# 2018/04/15

"""----------------------------"""

f = open('new1.txt','wt',encoding='utf8')
f.write('我載這哩痾痾痾ㄑ哥afkdlj')
# 15
f.close()
f = open('new1.txt','rt',encoding='utf8')
s = f.read()
print(s)

# 我載這哩痾痾痾ㄑ哥afkdlj

"""----------------------------"""

# 如何處理二進制文件
import struct
import array

f = open('demo.wav','rb')
info = f.read(44)

struct.unpack('h',info[22:24])
# (1,) 聲道數

struct.unpack('i',info[24:28])

# (44100,) 採樣頻率

struct.unpack('h',info[34:36])
# (8,) 編碼寬度


#計算文件長度
f.seek(0,2)
f.tell()
n = int((f.tell()-44)/2)


buf = array.array('h',(0 for i in range(n)))
f.seek(44)
f.readinto(buf)


for i in range(n):
    buf[i] /= 8
# 因 float 報錯   
    
f2 = open('demo2.wav','wb')

f2.write(info)

buf.tofile(f2)

f2.close()

"""----------------------------"""

# 如何訪問文件的狀態


import os

os.stat('new1.txt')

# 臨時文件
 
from tempfile import TemporaryFile,NamedTemporaryFile

f = TemporaryFile()

f.write(b'abdbdbbd' *10000)

ntf = NamedTemporaryFile()

