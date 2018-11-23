import re

s = "2008年发生了很多大事,08奥运,512大地震"
s = 'zhang:1994 li:1993'
# pattern = r'(\w+):(\d+)'
# pattern = r'\d+'
# l = re.findall(pattern,s)
# print(l)

# 用compile实现
s = "2008年发生了很多大事,08奥运,512大地震"
pattern = r'\d+'
# l = re.findall(pattern,s)
# print(l)
#相当于创建了一个正则表达式的对象,利用本身的方法直接操作
regex = re.compile(pattern)
l = regex.findall(s,0,18)
print(l)

# ==============================================
l = re.split(r'\s+',"hello world    NIhao beijing")
print(l)

# ========================
s = re.sub(r'\s+','##','hello world hi jame',2)
print(s)

# ==========================
s = re.subn(r'\s+','##','hello sfd dsfds',2)
print(s)

# =================================