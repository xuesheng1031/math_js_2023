
import matplotlib.pyplot as plt
from collections import OrderedDict, deque
import random
import copy
import csv

def read_csv(file_name):
    time_table_2 = []

    with open(file_name, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            # 使用map函数将每个元素转换为整数
            int_row = list(map(int, row))
            time_table_2.append(int_row)

    return time_table_2


time_table_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 60, 35, 30, 40],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 60, 35, 30, 50],
            [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
            [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
            [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
            [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
            [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
            [0, 0, 0, 0, 0, 0, 25, 120, 30, 40, 55, 45, 30, 15, 35, 70, 50, 30, 45],
            [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
            [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
            [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
            [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
            [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
            [0, 0, 0, 0, 0, 0, 30, 105, 20, 40, 55, 45, 30, 15, 40, 70, 50, 30, 55],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [30, 65, 30, 20, 15, 90, 40, 180, 60, 50, 80, 60, 30, 30, 45, 75, 45, 35, 60],
            [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
            [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
            [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
            [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
            [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
            [35, 70, 30, 20, 20, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 40, 65],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70],
            [40, 80, 30, 20, 30, 90, 35, 200, 60, 60, 80, 60, 30, 30, 50, 80, 45, 35, 70]]

time_table_2 = read_csv("2.csv")


class Device:
    def __init__(self, name, test_requirement_dict: dict):
        # {0: [0, ], 1: [0,], ...8: [40]}  #测试需求时间表
        self.name = name     # 设备名称
        self.test_requirement_dict= test_requirement_dict  # 测试需求表
        self.start_time = [0 for i in range(19)]  # 测试开始时间
        self.end_time = [0 for i in range(19)]  # 测试结束时间
        self.line_num = None  # 测试线号


class ProductionLine:
    def __init__(self, test_places_list: list, line_id: int, active_list: list):
        self.available_time_point = 0
        self.test_places_list = test_places_list
        self.available_time_queue = deque(maxlen=3)
        for i in range(3):
            self.available_time_queue.append(0)
        self.line_id = line_id
        self.active_list = active_list
        self.group_active_status = [0 for _ in range(19)]  # 新增属性，表示每个测试台的活动状态

    def test(self, device: Device):
        end_time = 0
        for test_place in self.test_places_list:
            if self.active_list[test_place.order] == 1:
                if test_place.order == 0:
                    device.start_time[0] = self.available_time_point
                    device.line_num = self.line_id
                test_place.test(device)
                if test_place.order in [1, 2, 3, 4]:  # 第2-5个测试台
                    self.group_active_status[0] = 1
                elif test_place.order in [7, 8, 9, 10]:  # 第8-11个测试台
                    self.group_active_status[1] = 1
                elif test_place.order in [11, 12, 13]:  # 第12-14个测试台
                    self.group_active_status[2] = 1
                elif test_place.order in [15, 16, 17]:  # 第16-18个测试台
                    self.group_active_status[3] = 1
                else:  # 第1、6、7、15、19个测试台
                    self.group_active_status[test_place.order] = 1
                if test_place.order == 18:
                    self.available_time_queue.append(sum(self.group_active_status))
                    self.group_active_status = [0 for _ in range(19)]  # 重置测试台组的活动状态
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
        if self.order <= 18:
            device.start_time[self.order + 1] = end_time

{2:[120, 65, 60, 15]}

class TestPlace2(TestPlace):
    def test(self, device: Device):
        time_load_list = device.test_requirement_dict[self.order]
        time_spent_total = time_load_list[0]
        if self.add_num == 2:
            return max(time_spent_total[-3:])
        if self.add_num == 1:
            poss_1 = time_load_list[-2] + time_spent_total[-3]
            poss_2 = time_spent_total[-1] + time_spent_total[-2]
            poss_3 = time_spent_total[-1] + time_spent_total[-3]
            return min(poss_1, poss_2, poss_3)
        if self.add_num == 0:
            return time_spent_total

class Factory:
    def __init__(self, production_line_list: list):
        self.production_line_list = production_line_list # 产线列表

    def test(self, device):
        # 产线列表按可用时间点排序
        self.production_line_list.sort(key=lambda x: x.available_time_point)
        # 选择可用时间点最小的产线
        self.production_line_list[0].test(device)
        # device.line_num = self.production_line_list[0].line_num


def c_max(order_list, if_return_load_table=True):
    # order_list = [0, 12, 23, 32, 40, 15, 6, 7, 8, ....  48,]
    # 生成设备列表
    device_list = []
    for i in range(48):
        time_talbe_row = time_table_2[i]
        req_dict = {}
        for j in range(19):
            req_dict[j] = time_talbe_row[j]
        device = Device(f'{i}', req_dict)
        device_list.append(device)

    device_test_list = [device_list[i] for i in order_list]    # 将设备按顺序排列
    # 连个设备测试线，分别包含19台设备
    active_list1 = [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 你的激活列表
    active_list2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 你的激活列表
    active_list = [0, 0, 1, 1, 0, 1, 1, 1, 1, 1]
    add_num = active_list[:2]
    line1_test_place2 = TestPlace2('line1_test_place2', 2, add_num)
    add_num = active_list[2:4]
    line2_test_place2 = TestPlace2('line2_test_place2', 2, add_num)
    add_num = active_list[5]
    production_line1 = ProductionLine([TestPlace(str(i), i, 0) for i in range(19)], 1, active_list1)
    production_line2 = ProductionLine([TestPlace(str(i), i, 0) for i in range(19)], 2, active_list2)
    factory = Factory([production_line1, production_line2])

    for device in device_test_list:
        factory.test(device)
    end_time = max([max(device.end_time) for device in device_test_list])
    print(end_time)
    if if_return_load_table:
        load_table = []
        for device in device_test_list:
            for i in range(19):
                load_table.append([device.name, device.line_num, i, [device.start_time[i], device.end_time[i]]])
        return load_table, end_time
    return end_time

if __name__ == '__main__':
    c_max([4, 19, 2, 6, 17, 23, 16, 29, 30, 3, 12, 43, 14, 37, 35, 24, 41, 39, 46, 27, 47, 45, 44, 34, 28, 42, 38, 36, 26, 33, 31, 40, 15, 25, 13, 32, 18, 21, 22, 11, 20, 8, 0, 10, 7, 9, 1, 5])


