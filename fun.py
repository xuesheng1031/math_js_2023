import matplotlib.pyplot as plt
from collections import OrderedDict
import random
import copy
import datetime
import numpy as np
import re
import matplotlib.pyplot as plt
import datetime

# plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
import eval_func2_xs
jobs = 48  # 工件数
population_num = 1000  # 种群规模
population = []  # 初始种群
variation_rate = 0.8  # 变异率
iters = 10  # 进化次数
target_points = [1, 2, 3]  # 变异靶点

# 初始化一个种群
for i in range(population_num):
    population.append(random.sample(range(0, jobs), jobs))

random.seed(0)


# 定义节点类state为当前解向量，封装当前解的排列方式，加工时间状况，最大加工时间以及适应度
class Node:
    def __init__(self, state):
        self.state = state
        # 真实的适应度函数
        end_time = eval_func2_xs.c_max(state)
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


def main():
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"file_{current_time}.txt"
    solution_list = []  # 存放noda解结点类
    for i in population:
        locals()['solution{}'.format(population.index(i))] = Node(i)
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
        cross_solution = [Node(i) for i in cross_population]
        solution_list = solution_list + cross_solution
        solution_list.sort(key=lambda x: x.end_time)
        with open(file_name, 'a') as f:
            f.write(f'{epoch}:{solution_list[0].state}:{[solution.end_time for solution in solution_list]}\n')
        del solution_list[population_num:]
    print('进化完成，最终最优加工时间为：', solution_list[0].end_time)
    end = datetime.datetime.now()
    print('耗时{}'.format(end - start))


if __name__ == '__main__':
    main()
