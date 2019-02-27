# yangli
names=['1q','21a']

for ind in names:
    print(ind)
names.append('3ee')
names.extend(names)

names[0]='sssssss'
names.insert(2,'wwwwww')
currIndex = '1q'
if currIndex in names:
    print('yes')
    print(names.index(currIndex,0,5))
else:
    print('not')
print(names)
del names[0]
print(names)
names.__delitem__(0)
print(names)

names.pop()
print(names)
print(names.count('1q'))

num =[1,2,4,3,1,8]
print(num)
num.sort()
print(num)
num.reverse()
print(num)

