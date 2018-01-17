# -------------------------File Handling
fo = open("sample.txt", "wb")
print("file name :", fo.name)
print("mode of opening :", fo.mode)
print("is closed :", fo.closed)
# print("softspace flag :", fo.softspace)
# -------------------------File writing
with open('sample.txt','wt') as f:
    f.write("this is 1st line\n")
    f.write("this is 2nd line\n")
    f.write("this is 3rd line\n")

# -------------------------File reading
with open('sample.txt') as f:
    data = f.read()
print (data)

# -------------------------File reading and iterate over the lines
with open('sample.txt') as f:
    for line in f:
        print(line, end='')

print("Python" , end = ' ')
print("GeeksforGeeks")