import matplotlib.pyplot as plt
import os
import numpy as np
from collections import defaultdict
# 定义文件夹路径
folder_path = '/Users/xs/PycharmProjects/math_lzy/4444'
# 获取文件夹中所有txt文件

# 获取文件夹中所有txt文件
files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]

# 检查文件数量
assert len(files) == 254, f"Expected 254 files, but found {len(files)} files."

data_points = defaultdict(list)

for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()

        # 获取第一行第三列的列表
        first_line_third_column = list(map(int, lines[0].strip().split(':')[2].strip('[]').split(',')))

        # 将列表转换为10位2进制数，并转换为10进制
        first_line_value = int(''.join(map(str, first_line_third_column)), 2)

        # 获取最后一行第三列的列表
        last_line_third_column = list(map(int, lines[-1].strip().split(':')[2].strip('[]').split(',')))

        # 计算最小值
        min_value = min(last_line_third_column)

        # 为每个x值收集所有对应的y值
        data_points[first_line_value].append(min_value)

# 对于每个x值，选择最小的y值
data_points = {x: min(y) for x, y in data_points.items()}

# 按照y的值对x，y排序，逆序排列使得y从大到小排序
data_points = sorted(data_points.items(), key=lambda x: x[1], reverse=True)

# 将排序后的data_points字典分解为x和y
x, y = zip(*data_points)

# 绘制折线图
plt.figure()
plt.stem(x, y)
plt.xlabel('samples', fontsize=15)
plt.ylabel('average time', fontsize=15)
plt.show()
