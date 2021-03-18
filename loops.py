
num = [1, 2, 3 , 4 , 5]

for i in num:
    print(i)

for j in num:
    if j == 3:
        print('Found!')
        break
    print(j)

for k in num:
    if k == 4 :
        print('Found!')
        continue
    print(k)

for l in num:
    for letter in 'abc':
        print(l, letter)

for m in range(10):
    print (m)

for n in range(1, 11):
    print(n)

x = 0
while x>-1:
    if x == 423678:
        break
    
    print (x)
    x += 1