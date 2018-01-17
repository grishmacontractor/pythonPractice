# ------------------------------------------for in loop with range
for x in range(0,3):
 print ("loop execution", x)
# ------------------------------------------for in loop with string
for letter in 'Grishma':
    print ('Current letter is', letter)
# ------------------------------------------while loop with string
count = 1
while count < 5:
    print ("Count is %d" % (count))
    count = count + 1
# ------------------------------------------nested loops
for g in range(1, 6):
    for k in range(1, 3):
        print('%d * %d = %d' % (g, k, g*k))
# -----------------------------------------using break
count = 0
while count <= 100:
    print('---------------',count)
    count += 1
    if count >= 3:
        break
# -----------------------------------------to check x is even then continue the loop and print odd
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
# ----------------------------------------using pass
for letter in 'TutorialsCloud':
    if letter == 'o':
        pass
        print('pass block')
        continue
    print ('current letter is :', letter)