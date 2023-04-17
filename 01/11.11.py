import numpy as np


# a = np.arange(20)  # 对比range()方法进行记忆  一维
# print(a)
# print(type(a))  # <class 'numpy.ndarray'>
# b = np.arange(20).reshape((5, 4))  # 二维
# c = np.arange(0, 24).reshape((2, 3, 4))  # 三维
# print(c)
# print(b)

# e = np.zeros((3, 3), dtype=np.uint8)  # 生成一个全为0的ndarray, 元素类型是整数
# print(e)
# f = a.astype(np.float64)  # 浮点型
# print(f)
# g = np.ones((4, 4), dtype=np.uint8)  # 生成一个全为1的ndarray, 元素类型是整数
# print(g)
# h = g.astype(np.float64)  # 浮点型
# print(h)


# a = np.repeat((3, 4, 5), 5)
# print(a)

"""
广播
"""
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[10, 10, 10], [20, 20, 20]])
# c = a*b
# print(c)
# print(a.shape, b.shape)

# 形状不同
# num1 = np.array([[1, 2, 3], [10, 10, 10], [20, 20, 20]])
# num2 = np.array([1, 2, 3])
# print(num1.shape)
# print(num2.shape)
# num3 = num1*num2
# print(num3)

a = np.array([30, 45, 60])
sin_num = np.sin(a * np.pi / 180)
cos_num = np.cos(a * np.pi / 180)
tan_num = np.tan(a * np.pi / 180)
print("正弦", sin_num)
print("余弦", cos_num)
print("正切", tan_num)
print("-=-=--=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
sin_ang = np.arcsin(sin_num)
cos_ang = np.arccos(cos_num)
tan_ang = np.arctan(tan_num)
print("反正弦", sin_ang)  # 反正弦 [0.52359878 0.78539816 1.04719755]
print("反余弦", cos_ang)  # 反余弦 [0.52359878 0.78539816 1.04719755]
print("反正切", tan_ang)  # 反正切 [0.52359878 0.78539816 1.04719755]

c = []
c.a

