import re
pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)

obj = regex.search("abcdefghi",0,7)
# print(obj.group())
#属性
print(obj.pos) #目标子串开始位置
print(obj.endpos) #目标子串结束位置
print(obj.re)   #正则表达式
print(obj.string)  #目标字符串
print(obj.lastgroup)  #最后一组组名
print(obj.lastindex)

print('==========================================')
print(obj.start())  #匹配内容的开始位置
print(obj.end())
print(obj.span())
