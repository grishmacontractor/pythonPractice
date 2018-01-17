# -------------------------tuples
tupl1 = ('compsrc', 'it' , 'cse')
tupl2 = (6,5,4,3,2,1)


print('tupl1[0]', tupl1[0])
print('tupl2[2:4]', tupl2[2:4])

print("updating tuples-------------")
tupl3 = tupl1 + tupl2
print(tupl3)

print("deleting tuples-------------")
del tupl3
