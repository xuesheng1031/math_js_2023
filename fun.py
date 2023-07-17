import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np
import re
import datetime
import itertools
from collections import OrderedDict, deque
import random
import copy
import csv


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


def c_max(order_list, active_list: list = None, if_return_load_table= False):
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





# plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

jobs = 48  # 工件数
population_num = 1000 # 种群规模
population = []  # 初始种群
variation_rate = 0.8  # 变异率
iters = 500  # 进化次数
target_points = [1, 2, 3]  # 变异靶点

# 初始化一个种群
for i in range(population_num):
    population.append(random.sample(range(0, jobs), jobs))

random.seed(0)


# 定义节点类state为当前解向量，封装当前解的排列方式，加工时间状况，最大加工时间以及适应度
class Node:
    def __init__(self, state, active_list : list = None):
        self.state = state
        # 真实的适应度函数
        self.active_list = active_list
        end_time = c_max(state, self.active_list)
        self.end_time = end_time


# PMX两点交叉函数
def two_points_cross(a1, a2):
    # 不改变原始数据进行操作
    a1_1 = copy.deepcopy(a1)
    a2_1 = copy.deepcopy(a2)
    # 交叉位置,point1<point2
    point1 = random.randint(0, len(a1_1))
    point2 = random.randint(0., len(a1_1))
    while point1 > point2 or point1 == point2:
        point1 = random.randint(0, len(a1_1))
        point2 = random.randint(0., len(a1_1))
    # 记录交叉项
    fragment1 = a1[point1:point2]
    fragment2 = a2[point1:point2]
    # 交叉
    a1_1[point1:point2], a2_1[point1:point2] = a2_1[point1:point2], a1_1[point1:point2]
    # 定义容器
    a1_2 = []  # 储存修正后的head
    a2_2 = []
    a1_3 = []  # 修正后的tail
    a2_3 = []
    # 子代1头部修正
    for i in a1_1[:point1]:
        while i in fragment2:
            i = fragment1[fragment2.index(i)]
        a1_2.append(i)
    # 子代2尾部修正
    for i in a1_1[point2:]:
        while i in fragment2:
            i = fragment1[fragment2.index(i)]
        a1_3.append(i)
    # 子代2头部修订
    for i in a2_1[:point1]:
        while i in fragment1:
            i = fragment2[fragment1.index(i)]
        a2_2.append(i)
    # 子代2尾部修订
    for i in a2_1[point2:]:
        while i in fragment1:
            i = fragment2[fragment1.index(i)]
        a2_3.append(i)

    child1 = a1_2 + fragment2 + a1_3
    child2 = a2_2 + fragment1 + a2_3
    # print('修正后的子代为:\n{}\n{}'.format(child1, child2))
    return child1, child2


# 交换变异
def gene_exchange(n):
    point1 = random.randint(0, len(n) - 1)
    point2 = random.randint(0, len(n) - 1)
    while point1 == point2 or point1 > point2:
        point1 = random.randint(0, len(n) - 1)
        point2 = random.randint(0, len(n) - 1)
    n[point1], n[point2] = n[point2], n[point1]
    return n


# 插入变异
def gene_insertion(n):
    point1 = random.randint(0, len(n) - 1)
    point2 = random.randint(0, len(n) - 1)
    while point1 == point2:
        point1 = random.randint(0, len(n) - 1)
        point2 = random.randint(0, len(n) - 1)
    x = n.pop(point1)
    n.insert(point2, x)
    return n


# 局部逆序变异
def gene_reverse(n):
    point1 = random.randint(0, len(n) - 1)
    point2 = random.randint(0, len(n) - 1)
    while point1 == point2 or point1 > point2:
        point1 = random.randint(0, len(n) - 1)
        point2 = random.randint(0, len(n) - 1)
    ls_res = n[point1:point2]
    ls_res.reverse()
    l1 = n[:point1]
    l2 = n[point2:]
    n_res_end = l1 + ls_res + l2
    return n_res_end


def main(active_list):
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"file_{current_time}.txt"
    solution_list = []  # 存放noda解结点类
    for i in population:
        locals()['solution{}'.format(population.index(i))] = Node(i, active_list)
        solution_list.append(locals()['solution{}'.format(population.index(i))])
    # 循环开始
    start = datetime.datetime.now()
    with open(file_name, 'a') as f:
        f.write(f'Null:Null:{active_list}\n')
    for epoch in range(iters):
        if epoch % 10 == 0:
            print('第{}次进化后的最优加工时间为{}, 最优顺序为{}'.format(epoch, solution_list[0].end_time, solution_list[0].state))
        pops = [i.state for i in solution_list]
        pop_children1 = pops[1::2]  # 偶数解
        pop_children2 = pops[::2]  # 奇数解
        # PMX两点交叉变异
        for i in range(len(pop_children1)):
            pop_children1[i], pop_children2[i] = two_points_cross(pop_children1[i], pop_children2[i])
        # 交叉后的子种群
        cross_population = pop_children1 + pop_children2
        # 变异
        for i in cross_population:
            mutation_rate = random.random()
            if mutation_rate > variation_rate:
                target = random.choice(target_points)
                if target == 1:
                    cross_population[cross_population.index(i)] = gene_exchange(i)
                elif target == 2:
                    cross_population[cross_population.index(i)] = gene_insertion(i)
                else:
                    cross_population[cross_population.index(i)] = gene_reverse(i)
        # 选择
        cross_solution = [Node(i, active_list) for i in cross_population]
        solution_list = solution_list + cross_solution
        solution_list.sort(key=lambda x: x.end_time)

        with open(file_name, 'a') as f:
            f.write(f'{epoch}:{solution_list[0].state}:{[solution.end_time for solution in solution_list]}\n')
        del solution_list[population_num:]
    print('进化完成，最终最优加工时间为：', solution_list[0].end_time)
    end = datetime.datetime.now()
    print('耗时{}'.format(end - start))


def main2():
    activation_lists = generate_activation_lists(num_elements=10, num_active=5)

    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"file_{current_time}.txt"

    for active_list in activation_lists:
        solution_list = []  # 存放noda解结点类
        for i in population:
            locals()['solution{}'.format(population.index(i))] = Node(i, active_list)
            solution_list.append(locals()['solution{}'.format(population.index(i))])
        # 循环开始
        start = datetime.datetime.now()
        for epoch in range(iters):
            if epoch % 10 == 0:
                print('第{}次进化后的最优加工时间为{}, 最优顺序为{}'.format(epoch, solution_list[0].end_time, solution_list[0].state))
            pops = [i.state for i in solution_list]
            pop_children1 = pops[1::2]  # 偶数解
            pop_children2 = pops[::2]  # 奇数解
            # PMX两点交叉变异
            for i in range(len(pop_children1)):
                pop_children1[i], pop_children2[i] = two_points_cross(pop_children1[i], pop_children2[i])
            # 交叉后的子种群
            cross_population = pop_children1 + pop_children2
            # 变异
            for i in cross_population:
                mutation_rate = random.random()
                if mutation_rate > variation_rate:
                    target = random.choice(target_points)
                    if target == 1:
                        cross_population[cross_population.index(i)] = gene_exchange(i)
                    elif target == 2:
                        cross_population[cross_population.index(i)] = gene_insertion(i)
                    else:
                        cross_population[cross_population.index(i)] = gene_reverse(i)
            # 选择
            cross_solution = [Node(i, active_list) for i in cross_population]
            solution_list = solution_list + cross_solution
            solution_list.sort(key=lambda x: x.end_time)
            with open(file_name, 'a') as f:
                f.write(f'{epoch}:{solution_list[0].state}:{[solution.end_time for solution in solution_list]}\n')
            del solution_list[population_num:]
        print('进化完成，最终最优加工时间为：', solution_list[0].end_time)
        end = datetime.datetime.now()
        print('耗时{}'.format(end - start))



if __name__ == '__main__':
    main([0, 1, 0, 0, 1, 1, 0, 1, 1, 0])
