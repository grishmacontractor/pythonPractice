import re
value = "cyberdyne"
g = re.search("(dy.*)",  value)
if g:
    print("search: ", g.group())

s = re.match("(vi.*)", value)
if s:
    print("match:", m.group())

value = "two 2 four 4 six 6"
res = re.split("\D+" , value)

for elements in res:
    print (elements)