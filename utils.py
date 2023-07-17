import itertools
import os
from collections import defaultdict

import matplotlib.pyplot as plt
from eval_func1 import c_max
import random


def draw_order_gantt(order_list):
    load_table, _ = c_max(order_list, if_return_load_table=True)

    def color():
        color_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        col = ''
        while not col:
            col = ''.join(random.choices(color_ls, k=6))
        return '#' + col

    colors = [color() for i in range(48)]

    fig, ax = plt.subplots()  # Create a figure and axes object

    for i in load_table:
        width = i[3][-1] - i[3][0]
        height = 1
        x = i[3][0]
        y = int(i[1] * 10 + i[2] + 1)
        color_index = int(i[0])

        if width > 0:  # Only add device number if width is non-zero
            ax.barh(y=int(y), width=width, height=height, left=x, color=colors[color_index], edgecolor='black')
            ax.text(x + width / 2, y, f' {int(i[0])}', ha='center',va='center', fontsize=8)  # Add the device number on top of the bar

    y_ticks = list(range(11,30))

    ax.set_yticks(y_ticks)  # Set the y ticks to the list of integers
    ax.set_yticklabels(y_ticks)  # Set the y tick labels to the list of integers

    plt.title('Optimal job scheduling strategy', fontsize=26)
    plt.xlabel('Time', fontsize=22)
    plt.ylabel('Device', fontsize=22)
    plt.show()


def draw_best_instance_chart():
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


def draw_order_gantt_pro(order_list):
    load_table, _ = c_max(order_list, active_list = [1, 0, 1, 0, 0, 1, 0, 1, 0, 1], if_return_load_table=True)

    def color():
        color_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        col = ''
        while not col:
            col = ''.join(random.choices(color_ls, k=6))
        return '#' + col

    colors = [color() for i in range(48)]

    fig, ax = plt.subplots()  # Create a figure and axes object

    for i in load_table:
        width = i[3][-1] - i[3][0]
        height = 1
        x = i[3][0]
        y = int(i[1] * 10 + i[2] + 1)
        color_index = int(i[0])

        if width > 0:  # Only add device number if width is non-zero
            ax.barh(y=int(y), width=width, height=height, left=x, color=colors[color_index], edgecolor='black')
            ax.text(x + width / 2, y, f' {int(i[0])}', ha='center',va='center', fontsize=8)  # Add the device number on top of the bar

    y_ticks = list(range(11,30))

    ax.set_yticks(y_ticks)  # Set the y ticks to the list of integers
    ax.set_yticklabels(y_ticks)  # Set the y tick labels to the list of integers

    plt.title('Optimal job scheduling strategy', fontsize=26)
    plt.xlabel('Time', fontsize=22)
    plt.ylabel('Device', fontsize=22)
    plt.show()


def draw_average_min_epoch():
    """
    Draw the maximum and average values of the processing time for every 400 generations.

    :return:
    """
    # Initialize x, y_min, y_avg as empty lists
    x = []
    y_min = []
    y_avg = []

    # Read the first 1500 lines from the txt file
    with open('/Users/xs/PycharmProjects/math_lzy/file_20230715_035015.txt', 'r') as f:
        line_count = 0
        for line in f:
            # Break the loop if line_count reaches 1500
            if line_count >= 1500:
                break

            # Increment line_count
            line_count += 1

            columns = line.strip().split(':')

            # Add x coordinate
            x.append(int(columns[0]))

            # Convert the string to a list
            y_data = list(map(int, columns[2].strip('[]').split(',')))

            # Calculate the minimum value
            y_min.append(min(y_data))

            # Calculate the average value
            y_avg.append(sum(y_data) / len(y_data))

    # Create the plot
    plt.figure()

    # Add the minimum value line
    plt.plot(x, y_min, label='Min')

    # Add the average value line
    plt.plot(x, y_avg, label='Avg')

    # Add the Y-axis title
    plt.ylabel('Processing Time', fontsize=15)

    # Add the X-axis label
    plt.xlabel('Genetic Generation', fontsize=15)

    # Add the legend
    plt.legend()

    # Annotate the current values at every 400 generations
    for i in range(0, len(x), 500):
        plt.annotate(f'Min: {y_min[i]}', (x[i], y_min[i]), textcoords="offset points", xytext=(0, -15), ha='center',
                     fontsize=15)
        plt.annotate(f'Avg: {y_avg[i]}', (x[i], y_avg[i]), textcoords="offset points", xytext=(0, 20), ha='center',
                     fontsize=15)

    # Show the plot
    plt.show()


def draw_four_max_min_value():
    """
    绘制四个文件的最大值和最小值

    :return:
    """
    # 定义文件名列表
    files = ['/Users/xs/PycharmProjects/math_lzy/111.txt',
             '/Users/xs/PycharmProjects/math_lzy/file_20230717_030011.txt',
             '/Users/xs/PycharmProjects/math_lzy/-1.txt',
             '/Users/xs/PycharmProjects/math_lzy/data.txt']

    # 定义颜色列表
    colors = ['r', 'g', 'b', 'y']

    plt.figure()

    for file_index in range(4):
        # Initialize x, y_min as empty lists
        x = []
        y_min = []

        # Read the first 1500 lines from the txt file
        with open(files[file_index], 'r') as f:
            line_count = 0
            for line in f:
                # Break the loop if line_count reaches 1500
                if line_count >= 150:
                    break

                # Increment line_count
                line_count += 1

                columns = line.strip().split(':')

                # Add x coordinate
                x.append(int(columns[0]))

                # Convert the string to a list
                y_data = list(map(int, columns[2].strip('[]').split(',')))

                # Calculate the minimum value
                y_min.append(min(y_data))

        # Add the minimum value line
        plt.plot(x, y_min, label=f'K {(file_index + 1) * 0.25} ', color=colors[file_index])

    # Add the Y-axis title
    plt.ylabel('Max Time', fontsize=15)

    # Add the X-axis label
    plt.xlabel(' ', fontsize=15)

    # Add the legend
    plt.legend()

    # Show the plot
    plt.show()


def generate_activation_lists(num_elements=10, num_active=5):
    # 生成一个0到num_elements-1的列表，表示元素的索引
    indices = list(range(num_elements))

    # 使用itertools找到所有可能的激活元素的组合
    active_combinations = list(itertools.combinations(indices, num_active))

    # 为每个组合生成一个激活列表
    activation_lists = []
    for active_indices in active_combinations:
        # 创建一个只包含0的列表
        activation_list = [0]*num_elements
        # 将激活元素的索引位置设为1
        for i in active_indices:
            activation_list[i] = 1
        # 添加到结果列表中
        activation_lists.append(activation_list)

    return activation_lists


if __name__ == '__main__':
    test_order = [4, 19, 2, 6, 17, 23, 16, 29, 30, 3, 12, 43, 14, 37, 35, 24, 41, 39, 46, 27, 47, 45,
                  44, 34, 28, 42, 38, 36, 26, 33, 31, 40, 15, 25, 13, 32, 18, 21, 22, 11, 20, 8, 0, 10,
                  7, 9, 1, 5]
    draw_order_gantt(test_order)