import re
s = 'Hi,This is Jame'
it = re.finditer(r'[A-Z]\w+',s)
print(next(it).group())
for i in it:
    print(i.group()) #获取match对象对应子串

# ========================
try:
    obj = re.fullmatch(r'\w+','port*123')
    print(obj.group())
except AttributeError as e:
    print(e)



# ====================================
obj = re.search(r'\d+','123-3700-4567')
print(obj.group())
