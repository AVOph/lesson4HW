from functools import reduce
def reducer_func(el_prev, el):
    return el_prev * el
num_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(reducer_func, num_list))
