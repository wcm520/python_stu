import numpy as np
def parse_data(num):
    if num:
        return int(num)
    else:
        return 0
dt = np.dtype([('age','i1'), ('height', 'i2')])
print(dt)
stu = np.loadtxt('has_empty_data.csv', dtype=dt, skiprows=1, delimiter=',', usecols=(1, 3), converters={1: parse_data,3:parse_data})
print(stu)
print(stu['age'], stu['age'].dtype)
# 求年龄的平均数
print('年龄平均数', np.mean(stu['age']))
print('平均身高', np.mean(stu['height']))
# 根据现实情况,学生年龄不会为0 为了减小误差,可以用中位数代替
# 中位数
ages = stu['age']
ages[ages == 0] = np.median(ages)
print(ages)
print('转化后年龄的平均数', '{:.2f}'.format(np.mean(ages)))
sg = stu['height']
sg[sg == 0] = np.median(sg)
print(sg)
print('转化后身高的平均数', '{:.2f}'.format(np.mean(sg)))

