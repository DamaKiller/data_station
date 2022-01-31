#元组与集合，列表，字典等等一样，保存的是对对象的引用。
#若引用的元素是可变的，即使元组本身不可变，元素依然可变。
#元组的不可变性指的是保存的引用不可变，与引用的对象无关

a = (1,2,[3,4])
b = (1,2,[3,4])
print(a == b)   #True
print(id(a[-1]))    #2092805344576
a[-1].append(5)
print(a)    #(1, 2, [3, 4, 5])
print(id(a[-1]))    #2092805344576
print(a == b)   #False