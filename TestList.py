
print("Test List")

#定义列表list
names = ["Jack", "Alice", "Lily"]
print(names)
print(type(names))


#通过下标(index)访问列表中的元素
print(names[0]);
print(names[1]);
print(names[2]);
# 下标越界 list index out of range
# print(names[3]);


#向列表的尾部添加元素
names.append("Rico")
print(names)

#向列表中指定的位置插入元素
#向列表中下标为0的位置插入元素
names.insert(0, "Tom")
print(names)


#删除指定位置的元素（按下标删）
names.pop(3)
print(names)

#删除指定元素（按内容删）
names.remove("Tom")
print(names)

#删除列表中所有元素
# names.clear();
# print(names)

#修改指定下标的元素
names[0] = "Jack01"
print(names)


#得到列表的长度length
print(len(names))