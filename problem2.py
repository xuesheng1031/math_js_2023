import multiprocessing
from sko.GA import GA


from problem1 import genetic_algorithm_order
from eval_func2 import c_max_with_structure_changed
from functools import partial
from utils import generate_activation_lists
from eval_func2 import gene_problem2


def exhaustive_algorithm_order(total_nums=48, iters=10, population_num=1000, variation_rate=0.8,
                               evaluate_func=c_max_with_structure_changed, is_parallel=True):
    active_lists = generate_activation_lists(10, 5)   # 生成所有可能的激活列表, 共C10/5种
    func_list = [partial(evaluate_func, **{'active_list': active_list}) for active_list in active_lists]
    if is_parallel:
        with multiprocessing.Pool() as pool:
            pool.map(partial(genetic_algorithm_order, total_nums, iters, population_num, variation_rate), func_list)
    else:
        for activate_list in active_lists:
            print("正在测试结构: ", activate_list)
            best_gene, best_fitness_value = genetic_algorithm_order(total_nums, iters, population_num, variation_rate,
                                                            partial(evaluate_func, **{'active_list': activate_list}))
            print("最佳基因: ", best_gene)
            print("最佳适应度值: ", best_fitness_value)


def genetic_algorithm_for_activate_list():
    upper_bound = 10 * [1]
    lower_bound = 10 * [0]
    ga = GA(func=gene_problem2,
            n_dim=10, size_pop=10, max_iter=100, lb=lower_bound, ub=upper_bound, precision=1)
    bext_x, best_y = ga.fit()
    print("最佳基因: ", bext_x)
    print("最佳适应度值: ", best_y)




if __name__ == '__main__':
    genetic_algorithm_for_activate_list()


