from collections import OrderedDict

import matplotlib.pyplot as plt
from fun import c_max
import random


# def draw_order_for_problem_1(order_list):
#     load_table, _ = c_max(order_list, if_return_load_table=True)
#
#     def color():  # 甘特图颜色生成函数
#         color_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#         col = ''
#         for i in range(6):
#             col += random.choice(color_ls)
#         return '#' + col
#
#     colors = [color() for i in range(48)]  # 甘特图颜色列表
#     for i in load_table:
#         print(i)
#         plt.barh(y=i[1] * 9 + i[2], left=i[3][0], width=i[3][-1] - i[3][0], height=0.5, color=colors[int(i[0])],
#                  label=f'Device {i[0]}')
#     # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
#     # plt.rcParams['font.serif'] = ['KaiTi']
#     plt.rcParams['axes.unicode_minus'] = False
#     plt.title('Optimal job scheduling strategy')
#     plt.xlabel('Time')
#     plt.ylabel('device')
#     handles, labels = plt.gca().get_legend_handles_labels()  # 标签去重
#     by_label = OrderedDict(zip(labels, handles))
#     plt.legend(by_label.values(), by_label.keys())
#     plt.show()

# 除y轴完美
# def draw_order_for_problem_1(order_list):
#     load_table, _ = c_max(order_list, if_return_load_table=True)
#
#     def color():
#         color_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#         col = ''
#         while not col:
#             col = ''.join(random.choices(color_ls, k=6))
#         return '#' + col
#
#     colors = [color() for i in range(48)]
#
#     fig, ax = plt.subplots()  # Create a figure and axes object
#
#     for i in load_table:
#         width = i[3][-1] - i[3][0]
#         height = 1
#         x = i[3][0]
#         y = i[1] * 9 + i[2] + height / 2
#         color_index = int(i[0])
#
#         if width > 0:  # Only add device number if width is non-zero
#             ax.barh(y=y, width=width, height=height, left=x, color=colors[color_index])
#             ax.text(x + width / 2, y, f' {int(i[0])}', ha='center',va='center', fontsize=6)  # Add the device number on top of the bar
#
#     plt.title('Optimal job scheduling strategy')
#     plt.xlabel('Time')
#     plt.ylabel('Device')
#     plt.show()

#完美版本
def draw_order_for_problem_1(order_list):
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




if __name__ == '__main__':
    test_order = [10, 15, 44, 8, 16, 39, 40, 43, 41, 45, 25, 34, 35, 47, 36, 26, 37, 18, 30, 32, 31, 42, 38, 46, 24, 28, 27, 29, 33, 21, 17, 11, 23, 22, 19, 13, 20, 14, 1, 12, 4, 2, 7, 0, 9, 6, 5, 3]
    draw_order_for_problem_1(test_order)