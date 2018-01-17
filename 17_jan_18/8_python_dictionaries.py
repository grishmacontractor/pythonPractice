# -------------------------dictionary
dicto = {'Bookname':'Famous Five', 'Price' : 20 }
print(dicto)
print (dicto['Bookname'])
print (dicto['Price'])

new_dict = dict()
print(new_dict)

dict1 ={}
print(dict1)
dict1['First'] = 10
dict1['Second'] = 20
print(dict1)

print('updating')
dict1['First'] = 30
print(dict1)


print('deleting')
del dict1['First']
print(dict1)

print('clearing dicto dictionary')
dicto.clear();
print(dicto)

print('deleting dicto dictionary')
del dicto