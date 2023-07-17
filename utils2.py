from collections import OrderedDict

import matplotlib.pyplot as plt
from eval_func1 import c_max
import random


def draw_order_for_problem_1(order_list):
    load_table, _ = c_max(order_list, if_return_load_table=True)

    def color():
        color_ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        col = ''
        while not col:
            col = ''.join(random.choices(color_ls, k=6))
        return '#' + col

    colors = [color() for i in range(48)]
    fig, ax = plt.subplots()  # Create a figure and axes object

    for repeat in range(3):  # Repeat the plotting 3 times
        for i in load_table:
            width = i[3][-1] - i[3][0]
            height = 1
            x = i[3][0] + repeat * 2500  # Adding an offset for each repeat
            y = int(i[1] * 10 + i[2] + 1)
            color_index = int(i[0])

            if width > 0:  # Only add device number if width is non-zero
                ax.barh(y=int(y), width=width, height=height, left=x, color=colors[color_index], edgecolor='black')
                # ax.text(x + width / 2, y, f' {int(i[0])}', ha='center',va='center', fontsize=8)  # Add the device number on top of the bar

    y_ticks = list(range(11,30))

    ax.set_yticks(y_ticks)  # Set the y ticks to the list of integers
    ax.set_yticklabels(y_ticks)  # Set the y tick labels to the list of integers

    plt.title('Optimal job scheduling strategy', fontsize=26)
    plt.xlabel('Time', fontsize=22)
    plt.ylabel('Device', fontsize=22)
    plt.show()


if __name__ == '__main__':
    test_order = [4, 19, 2, 6, 17, 23, 16, 29, 30, 3, 12, 43, 14, 37, 35, 24, 41, 39, 46, 27, 47, 45, 44, 34, 28, 42, 38, 36, 26, 33, 31, 40, 15, 25, 13, 32, 18, 21, 22, 11, 20, 8, 0, 10, 7, 9, 1, 5]
    draw_order_for_problem_1(test_order)

