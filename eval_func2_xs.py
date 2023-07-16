import itertools

import matplotlib.pyplot as plt
from collections import OrderedDict, deque
import random
import copy
import csv

# def read_csv(file_name):
#     time_table_2 = []
#
#     with open(file_name, 'r', encoding='utf-8-sig') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             # 使用map函数将每个元素转换为整数
#             int_row = list(map(int, row))
#             time_table_2.append(int_row)
#
#     return time_table_2


# time_table_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
#             [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
#             [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
#             [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
#             [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
#             [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
#             [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
#             [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
#             [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
#             [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
#             [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
#             [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
#             [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
#             [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
#             [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
#             [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
#             [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
#             [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
#             [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
#             [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70]]
#
# # time_table_2 = read_csv("2.csv")
# new_data = []
# for row in time_table_2:
#     new_row = [row[:2] + [row[2:5]] + row[5:8] + [row[8:11]] + row[11:12] + [row[12:14]] + row[14:16] + [row[16:18]] + row[18:]]
#     new_data.append(new_row)
#
# time_table_2 = new_data
# print(time_table_2)

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


class Device:
    def __init__(self, name, test_requirement_dict: dict):
        # {0: [0, ], 1: [0,], ...8: [40]}  #测试需求时间表
        self.name = name     # 设备名称
        self.test_requirement_dict= test_requirement_dict  # 测试需求表
        self.start_time = [0 for i in range(9)]  # 测试开始时间
        self.end_time = [0 for i in range(9)]  # 测试结束时间
        self.line_num = None  # 测试线号


class ProductionLine:
    def __init__(self, test_places_list: list, line_id: int):
        self.available_time_point = 0  # 可用时间点
        self.test_places_list = test_places_list  # 测试位列表
        self.available_time_queue = deque(maxlen=3)  # 可承载最大为3
        for i in range(3):
            self.available_time_queue.append(0)
        self.line_id = line_id  # 生产线编号

    def test(self, device: Device):
        end_time = 0
        for test_place in self.test_places_list:
            # 根据最新允许上线时间上线
            if test_place.order == 0:
                device.start_time[0] = self.available_time_point
                device.line_num = self.line_id
            # 进行设备测试
            test_place.test(device)
            if test_place.order == 8:
                # 第9个测试位测试完成，更新生产线可用队列
                self.available_time_queue.append(test_place.available_time_point)
            self.available_time_point = min(self.available_time_queue)





class TestPlace:
    def __init__(self, name, order, add_num):
        self.name = name # 测试位名称
        self.order = order # 所在位置
        self.add_num = add_num # 扩建数量
        self.available_time_point = 0  # 可用时间点
        self._test_record = [] # 测试记录

    def test_spent(self, device: Device):
        return device.test_requirement_dict[self.order]

    def test(self, device: Device):
        # 计算所需时间
        time_spent = self.test_spent(device)
        # 开始于设备上一轮结束或者本设备可获得的最早时间当中的较大的那个
        start_time = max(device.start_time[self.order], self.available_time_point)
        end_time = start_time + time_spent
        # 记录测试记录
        self._test_record.append([device.name, start_time, end_time])
        # 更新设备测试的实际开始时间
        device.start_time[self.order] = start_time
        # 更新可用时间点
        self.available_time_point = end_time
        # 更新设备测试的结束时间以及下一轮最快开始时间
        device.end_time[self.order] = end_time
        if self.order <= 7:
            device.start_time[self.order + 1] = end_time

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
            time_spent =  min(poss_1, poss_2, poss_3)
        if self.add_num == 0:
            time_spent = time_load_list[0]
        return time_spent
class TestPlace5(TestPlace):
    def test_spent(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent = time_load_list[0]
        if self.add_num == 1:
            time_spent =  max(time_load_list[1] + time_load_list[2], time_load_list[3])
        if self.add_num == 0:
            time_spent =  time_load_list[0]
        return time_spent


class TestPlace6(TestPlace):
    def test_spent(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent = time_load_list[0]
        if self.add_num == 1:
            time_spent =  max(time_load_list[1], time_load_list[2])
        if self.add_num == 0:
            time_spent =  time_load_list[0]
        return time_spent
class TestPlace8(TestPlace):
    def test_spent(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent = time_load_list[0]
        if self.add_num == 1:
            time_spent =  max(time_load_list[1], time_load_list[2])
        if self.add_num == 0:
            time_spent =  time_load_list[0]
        return time_spent

class Factory:
    def __init__(self, production_line_list: list):
        self.production_line_list = production_line_list # 产线列表

    def test(self, device):
        # 产线列表按可用时间点排序
        self.production_line_list.sort(key=lambda x: x.available_time_point)
        # 选择可用时间点最小的产线
        self.production_line_list[0].test(device)
        # device.line_num = self.production_line_list[0].line_num


def c_max(order_list, if_return_load_table= False, active_list: list = None):
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
    TestPlace6('5', 5, add_num16),
    TestPlace('6', 6, 0),
    TestPlace8('7', 7, add_num18),
    TestPlace('8', 8, 0)
], 1)

    production_line2 = ProductionLine([
    TestPlace('0', 0, 0),
    TestPlace2('1', 1, add_num22),
    TestPlace('2', 2, 0),
    TestPlace('3', 3, 0),
    TestPlace5('4', 4, add_num25),
    TestPlace6('5', 5, add_num26),
    TestPlace('6', 6, 0),
    TestPlace8('7', 7, add_num28),
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

def c_max2(order_list, if_return_load_table= False):
    indices = list(range(10))

    # 使用itertools找到所有可能的激活元素的组合
    active_combinations = list(itertools.combinations(indices, 5))

    # 为每个组合生成一个激活列表
    activation_lists = []
    for active_indices in active_combinations:
        # 创建一个只包含0的列表
        activation_list = [0]*10
        # 将激活元素的索引位置设为1
        for i in active_indices:
            activation_list[i] = 1
        end_time = c_max(order_list, if_return_load_table, activation_list)
    return end_time



if __name__ == '__main__':
    c_max([4, 19, 2, 6, 17, 23, 16, 29, 30, 3, 12, 43, 14, 37, 35, 24, 41, 39, 46, 27, 47, 45, 44, 34, 28, 42, 38, 36, 26, 33, 31, 40, 15, 25, 13, 32, 18, 21, 22, 11, 20, 8, 0, 10, 7, 9, 1, 5])


