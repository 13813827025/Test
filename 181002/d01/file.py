# yangli
f = open('test.txt', 'w')

f.write('hello world, i am here!')

f.close()

d = open('test.txt')

print(d.readlines())
for i,da in d.readlines():
    print(i,da)

