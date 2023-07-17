import itertools
from collections import deque
from functools import partial

from eval_func1 import Device, TestPlace, Factory, ProductionLine
from problem1 import genetic_algorithm_order

# 题目中给出的数据
time_table_2 = [[0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 25, [60, 35, 30], 40],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 25, [60, 35, 30], 40],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 25, [60, 35, 30], 40],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 25, [60, 35, 30], 40],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 25, [60, 35, 30], 40],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 25, [60, 35, 30], 40],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 30, [60, 35, 30], 50],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 30, [60, 35, 30], 50],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 30, [60, 35, 30], 50],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 30, [60, 35, 30], 50],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 30, [60, 35, 30], 50],
               [0, [0, 0, 0, 0], 0, 0, [0, 0, 0, 0], [0, 0, 0], 30, [60, 35, 30], 50],
               [0, [0, 0, 0, 0], 0, 25, [120, 30, 40, 55], [45, 30, 15], 35, [70, 50, 30], 45],
               [0, [0, 0, 0, 0], 0, 25, [120, 30, 40, 55], [45, 30, 15], 35, [70, 50, 30], 45],
               [0, [0, 0, 0, 0], 0, 25, [120, 30, 40, 55], [45, 30, 15], 35, [70, 50, 30], 45],
               [0, [0, 0, 0, 0], 0, 25, [120, 30, 40, 55], [45, 30, 15], 35, [70, 50, 30], 45],
               [0, [0, 0, 0, 0], 0, 25, [120, 30, 40, 55], [45, 30, 15], 35, [70, 50, 30], 45],
               [0, [0, 0, 0, 0], 0, 25, [120, 30, 40, 55], [45, 30, 15], 35, [70, 50, 30], 45],
               [0, [0, 0, 0, 0], 0, 30, [105, 20, 40, 55], [45, 30, 15], 40, [70, 50, 30], 55],
               [0, [0, 0, 0, 0], 0, 30, [105, 20, 40, 55], [45, 30, 15], 40, [70, 50, 30], 55],
               [0, [0, 0, 0, 0], 0, 30, [105, 20, 40, 55], [45, 30, 15], 40, [70, 50, 30], 55],
               [0, [0, 0, 0, 0], 0, 30, [105, 20, 40, 55], [45, 30, 15], 40, [70, 50, 30], 55],
               [0, [0, 0, 0, 0], 0, 30, [105, 20, 40, 55], [45, 30, 15], 40, [70, 50, 30], 55],
               [0, [0, 0, 0, 0], 0, 30, [105, 20, 40, 55], [45, 30, 15], 40, [70, 50, 30], 55],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [30, [65, 30, 20, 15], 90, 40, [180, 60, 50, 80], [60, 30, 30], 45, [75, 45, 35], 60],
               [35, [70, 30, 20, 20], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 40], 65],
               [35, [70, 30, 20, 20], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 40], 65],
               [35, [70, 30, 20, 20], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 40], 65],
               [35, [70, 30, 20, 20], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 40], 65],
               [35, [70, 30, 20, 20], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 40], 65],
               [35, [70, 30, 20, 20], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 40], 65],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70],
               [40, [80, 30, 20, 30], 90, 35, [200, 60, 60, 80], [60, 30, 30], 50, [80, 45, 35], 70]]


class TestPlace2(TestPlace):
    def test_spent(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent = time_load_list[0]
        if self.add_num == 2:
            time_spent = max(time_load_list[-3:])
        if self.add_num == 1:
            poss_1 = max(time_load_list[1] + time_load_list[2], time_load_list[3])
            poss_2 = max(time_load_list[1] + time_load_list[3], time_load_list[2])
            poss_3 = max(time_load_list[2] + time_load_list[3], time_load_list[1])
            time_spent = min(poss_1, poss_2, poss_3)
        if self.add_num == 0:
            time_spent = time_load_list[0]
        return time_spent


class TestPlace5(TestPlace):
    def test_spent(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent = time_load_list[0]
        if self.add_num == 1:
            time_spent = max(time_load_list[1] + time_load_list[2], time_load_list[3])
        if self.add_num == 0:
            time_spent = time_load_list[0]
        return time_spent


class TestPlaceWith2Process(TestPlace):
    def test_spent(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent = time_load_list[0]
        if self.add_num == 1:
            time_spent = max(time_load_list[1], time_load_list[2])
        if self.add_num == 0:
            time_spent = time_load_list[0]
        return time_spent


def c_max_with_structure_changed(order_list, active_list: list = None, if_return_load_table=False, ):
    # order_list = [0, 12, 23, 32, 40, 15, 6, 7, 8, ....  48,]
    # 生成设备列表
    device_list = []
    for i in range(48):
        time_talbe_row = time_table_2[i]
        req_dict = {}
        for j in range(9):
            req_dict[j] = time_talbe_row[j]
        device = Device(f'{i}', req_dict)
        device_list.append(device)

    device_test_list = [device_list[i] for i in order_list]    # 将设备按顺序排列
    # active_list = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
    add_num12 = active_list[0] + active_list[1]
    add_num15 = active_list[2]
    add_num16 = active_list[3]
    add_num18 = active_list[4]
    add_num22 = active_list[5] + active_list[6]
    add_num25 = active_list[7]
    add_num26 = active_list[8]
    add_num28 = active_list[9]
    production_line1 = ProductionLine([
    TestPlace('0', 0, 0),
    TestPlace2('1', 1, add_num12),
    TestPlace('2', 2, 0),
    TestPlace('3', 3, 0),
    TestPlace5('4', 4, add_num15),
    TestPlaceWith2Process('5', 5, add_num16),
    TestPlace('6', 6, 0),
    TestPlaceWith2Process('7', 7, add_num18),
    TestPlace('8', 8, 0)
], 1)
    production_line2 = ProductionLine([
    TestPlace('0', 0, 0),
    TestPlace2('1', 1, add_num22),
    TestPlace('2', 2, 0),
    TestPlace('3', 3, 0),
    TestPlace5('4', 4, add_num25),
    TestPlaceWith2Process('5', 5, add_num26),
    TestPlace('6', 6, 0),
    TestPlaceWith2Process('7', 7, add_num28),
    TestPlace('8', 8, 0)
], 2)
    factory = Factory([production_line1, production_line2])

    for device in device_test_list:
        factory.test(device)
    end_time = max([max(device.end_time) for device in device_test_list])
    # print(end_time)
    if if_return_load_table:
        load_table = []
        for device in device_test_list:
            for i in range(9):
                load_table.append([device.name, device.line_num, i, [device.start_time[i], device.end_time[i]]])
        return load_table, end_time
    return end_time


def filter_more_than_five(func):
    """
    过滤掉基因总和大于5的基因
    :param func:
    :return:
    """
    def wraper(*args, **kwargs):
        if sum(args[0]) > 5:
            return float('inf')
        else:
            return func(*args, **kwargs)
    return wraper


@filter_more_than_five
def gene_problem2(activate_list):
    """
    问题2的基因函数
    :param activate_list:
    :return:
    """
    total_nums = 48
    iters = 10
    population_num = 10
    variation_rate = 0.8
    evaluate_func = c_max_with_structure_changed
    best_fitness_value, best_gene = genetic_algorithm_order(total_nums, iters, population_num, variation_rate,
                                                            partial(evaluate_func, **{'active_list': activate_list}))
    return best_fitness_value




if __name__ == '__main__':
    order_list = [4, 19, 2, 6, 17, 23, 16, 29, 30, 3, 12, 43, 14, 37, 35, 24, 41, 39, 46, 27, 47, 45, 44, 34,
                  28, 42, 38, 36, 26, 33, 31, 40, 15, 25, 13, 32, 18, 21, 22, 11, 20, 8, 0, 10, 7, 9, 1, 5]
    c_max_with_structure_changed(order_list, active_list=[1, 0, 1, 0, 1, 0, 0, 1, 0, 1], if_return_load_table=True)


