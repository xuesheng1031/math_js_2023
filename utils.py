from collections import OrderedDict

import matplotlib.pyplot as plt
from eval_func1 import c_max
import random


def draw_order_for_problem_1(order_list):
    load_table, _ = c_max(order_list, if_return_load_table=True)

    def color():  # 甘特图颜色生成函数
        color_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        col = ''
        for i in range(6):
            col += random.choice(color_ls)
        return '#' + col

    colors = [color() for i in range(48)]  # 甘特图颜色列表
    for i in load_table:
        print(i)
        plt.barh(y=i[1] * 9 + i[2], left=i[3][0], width=i[3][-1] - i[3][0], height=0.5, color=colors[int(i[0])],
                 label=f'Device {i[0]}')
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    # plt.rcParams['font.serif'] = ['KaiTi']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('Optimal job scheduling strategy')
    plt.xlabel('Time')
    plt.ylabel('device')
    handles, labels = plt.gca().get_legend_handles_labels()  # 标签去重
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.show()


if __name__ == '__main__':
    test_order = [9, 5, 18, 8, 4, 20, 16, 15, 33, 24, 47, 46, 17, 35, 30, 38, 42, 36, 27, 37, 19, 44, 3, 32, 23, 21, 7, 22, 34, 12, 40, 41, 39, 29, 45, 25, 11, 0, 13, 26, 43, 1, 14, 31, 28, 2, 6, 10]
    draw_order_for_problem_1(test_order)