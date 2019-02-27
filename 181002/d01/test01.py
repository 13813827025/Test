# yangli

print( 1121)

name =input("姓名:")
age =int(input("年龄："))

info2 ='''
    ---------- {name}------
    姓名：{name}
    年龄：{age}

'''.format(name=name,age=age)


info3='''
    -----{0}----
    姓名：{0}
    年龄：{1}    
'''.format(name,age)
print(info2)
print(info3)