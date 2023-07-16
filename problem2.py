import itertools

def generate_all_active_lists():
    # 初始化激活列表，其中第1、6、7、15、19、2、8、12、16位一直为1
    base_list = [0 for _ in range(19)]
    for i in [0, 1, 5, 6, 7, 11, 14, 15, 18]:
        base_list[i] = 1

    # 在第3-5、9-11、13-14、17-18位中，生成所有可能的5个位置的组合
    positions = list(range(2, 5)) + list(range(10, 11)) + list(range(12, 14)) + list(range(16, 18))  # 将第9和10位绑定在一起
    all_combinations = list(itertools.combinations(positions, 5))

    all_active_lists = []
    for combination in all_combinations:
        active_list1 = base_list.copy()
        active_list2 = base_list.copy()
        for pos in combination:
                active_list1[pos] = 1
                active_list2[pos] = 1
        all_active_lists.append((active_list1, active_list2))

    return all_active_lists

# 生成所有可能的激活列表
all_active_lists = generate_all_active_lists()

for active_list1, active_list2 in all_active_lists:
    print('active_list1',active_list1)
    print('active_list2',active_list2)


num_active_lists = len(all_active_lists)
print(f'Generated {num_active_lists} pairs of active lists.')
