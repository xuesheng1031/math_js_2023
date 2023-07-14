
import matplotlib.pyplot as plt
from collections import OrderedDict, deque
import random
import copy

time_table = [[0, 0, 0, 0, 0, 0, 25, 60, 40],
              [0, 0, 0, 0, 0, 0, 25, 60, 40],
              [0, 0, 0, 0, 0, 0, 25, 60, 40],
              [0, 0, 0, 0, 0, 0, 25, 60, 40],
              [0, 0, 0, 0, 0, 0, 25, 60, 40],
              [0, 0, 0, 0, 0, 0, 25, 60, 40],
              [0, 0, 0, 0, 0, 0, 30, 60, 50],
              [0, 0, 0, 0, 0, 0, 30, 60, 50],
              [0, 0, 0, 0, 0, 0, 30, 60, 50],
              [0, 0, 0, 0, 0, 0, 30, 60, 50],
              [0, 0, 0, 0, 0, 0, 30, 60, 50],
              [0, 0, 0, 0, 0, 0, 30, 60, 50],
              [0, 0, 0, 25, 120, 45, 35, 70, 45],
              [0, 0, 0, 25, 120, 45, 35, 70, 45],
              [0, 0, 0, 25, 120, 45, 35, 70, 45],
              [0, 0, 0, 25, 120, 45, 35, 70, 45],
              [0, 0, 0, 25, 120, 45, 35, 70, 45],
              [0, 0, 0, 25, 120, 45, 35, 70, 45],
              [0, 0, 0, 30, 105, 45, 40, 70, 55],
              [0, 0, 0, 30, 105, 45, 40, 70, 55],
              [0, 0, 0, 30, 105, 45, 40, 70, 55],
              [0, 0, 0, 30, 105, 45, 40, 70, 55],
              [0, 0, 0, 30, 105, 45, 40, 70, 55],
              [0, 0, 0, 30, 105, 45, 40, 70, 55],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [30, 65, 90, 40, 180, 60, 45, 75, 60],
              [35, 70, 90, 35, 200, 60, 50, 80, 65],
              [35, 70, 90, 35, 200, 60, 50, 80, 65],
              [35, 70, 90, 35, 200, 60, 50, 80, 65],
              [35, 70, 90, 35, 200, 60, 50, 80, 65],
              [35, 70, 90, 35, 200, 60, 50, 80, 65],
              [35, 70, 90, 35, 200, 60, 50, 80, 65],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70],
              [40, 80, 90, 35, 200, 60, 50, 80, 70]]
# random.seed(0)


class Device:
    def __init__(self, name, test_requirement_dict: dict):
        # {0: [0, ], 1: [0,], ...8: [40]}  #测试需求时间表
        self.name = name # 设备名称
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


class Factory:
    def __init__(self, production_line_list: list):
        self.production_line_list = production_line_list # 产线列表

    def test(self, device):
        # 产线列表按可用时间点排序
        self.production_line_list.sort(key=lambda x: x.available_time_point)
        # 选择可用时间点最小的产线
        self.production_line_list[0].test(device)
        # device.line_num = self.production_line_list[0].line_num


def c_max(order_list, if_return_load_table=False):
    # order_list = [0, 12, 23, 32, 40, 15, 6, 7, 8, ....  48,]
    # 生成设备列表
    device_list = []
    for i in range(48):
        time_talbe_row = time_table[i]
        req_dict = {}
        for j in range(9):
            req_dict[j] = time_talbe_row[j]
        device = Device(f'{i}', req_dict)
        device_list.append(device)

    device_test_list = [device_list[i] for i in order_list]    # 将设备按顺序排列
    # 连个设备测试线，分别包含9台设备
    production_line1 = ProductionLine([TestPlace(str(i), i, 0) for i in range(9)], 1)
    production_line2 = ProductionLine([TestPlace(str(i), i, 0) for i in range(9)], 2)
    factory = Factory([production_line1, production_line2])

    for device in device_test_list:
        factory.test(device)
    end_time = max([max(device.end_time) for device in device_test_list])
    if if_return_load_table:
        load_table = []
        for device in device_test_list:
            for i in range(9):
                load_table.append([device.name, device.line_num, i, [device.start_time[i], device.end_time[i]]])
        return load_table, end_time
    return end_time



