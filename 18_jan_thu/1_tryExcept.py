from builtins import print

(a,b) = (6,0)
try:
    g = a/b
except ZeroDivisionError as s:
    k = s
    print(k)