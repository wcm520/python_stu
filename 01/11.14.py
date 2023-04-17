import numpy as np


"""
    舍入函数
    around 四舍五入1.数值2.舍入的小数位数：默认0
    floor函数 向下取整数
    ceil函数 向上取整数
"""

a = np.array([20.3, 30.63, 40.856, 40.2345])
print(a)
print('四舍五入', np.around(a))
print('向下取整数', np.floor(a))
print('向上取整数', np.ceil(a))



"""
算数
"""
b = np.arange(9, dtype=np.float64).reshape(3, 3)
c = np.array([10, 10, 10])
print(c)
print('add相加', np.add(b, c))
print('subtract相减', np.subtract(b, c))
print('multiply相乘', np.multiply(b, c))
print('divide相除', np.divide(b, c))

d = np.array([0.25, 1.33, 1, 100])
print('倒数', np.reciprocal(d))
e = np.array([10, 100, 1000])
print('次方', np.power(e, 3))
# 两数组余数
num1 = np.array([10, 20, 30])
num2 = np.array([3, 5, 7])
print('两数组余数', np.mod(num1, num2))

"""
统计函数 从数组中快速查询最小、最大、百分位标准差、方差等amin()参数:axis 1行比、0列比amaxptp() 最大值-最小值的差percentile0度量，百分比 1.数组 2.半分比 0-100 3.axismedian() 计算数组的 (中位数)中值mean() 算数平均值
std() 标准差 sqrt(mean(x-x. mean0)**2)标准差是一组数组的平均值分散成都的一种度量标准差应用于投资上，可作为量度回报稳定性的指标。标准差数值憾大，代表回报远离过去平均数值，回报较不稳定故风险憾高。相反，标准差数var() 方差 moan((xx,mean())**2)平均数之差的平方的平均数衡量随机变量或一组数据时离散程度的度量
求和 ndarray.sum@axis=0,从上往下查找:,ml.sum(axis=0)axis=1,从左往右查找’,m1.sum(axis=1)
加权平均值 numpyaverage0)即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数numpy.average(a, axis=None. weights=None. returmed=False)- weights: 数组，可选
与  中的值关联的权重数组。 中的每个值都根据其关联的权重对平均值做出贡献。权重数组可以是一维的(在这种情况下，它的长度必须是沿给
avg = sum(a * weights) / sum(weights)
对权重的唯一限制是 sum(weights) 不能为 0.
"""

# 方差


