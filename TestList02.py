
# 列表

age = 10
print(type(age))

score = 0.6
print(type(score))

name = 'cjl'
print(type(name))


#复合类型
#列表list
names = ['Jack', 'Alice', 'Lily']
print(type(names))

#打印列表
print(names)
#打印列表中指定下标的元素
print(names[0])
print(names[1])
print(names[2])
#报错列表下标越界（list index out of range）
# print(names[3])

#length 列表的长度（列表中元素的数量）
print(len(names))
#向列表中添加元素（追加到表尾）
names.append('Rico')
print(names)

#向列表的某个位置插入一个元素
names.insert(0, "Ivy")
print(names)

#删除列表中的元素
names.remove('Lily')
print(names)

#删除指定位置的元素
print(names.pop(0))
print(names)

names[0] = 'Jack01'
print(names)

