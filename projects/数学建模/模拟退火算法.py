import math
import random

def simulated_annealing(func, init_state, init_temp, cool_rate, iter_per_temp):
    current_state = init_state
    current_temp = init_temp

    while current_temp > 0.01:
        for _ in range(iter_per_temp):
            new_state = get_neighbor(current_state)
            delta = func(new_state) - func(current_state)

            if delta < 0 or random.random() < math.exp(-delta / current_temp):
                current_state = new_state

        current_temp *= cool_rate

    return current_state

def get_neighbor(state):
    # 这个函数应该根据你的问题生成一个邻居状态
    pass