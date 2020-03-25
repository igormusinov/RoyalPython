# %%
import multiprocessing as mp
from multiprocessing import Pool

from time import sleep

from datetime import datetime


# %%
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        delta = (datetime.now() - start)
        return delta, result

    return wrapper


# @timeit
def func(*args, **kwargs):
    # mp.current_process()
    sleep(1)
    return 1


def wrap_func(*args, **kwargs):
    print("Begin")
    func(*args, **kwargs)


#     print("End")

def multiproc_test(proc_num: int, function, args):
    start = datetime.now()
    with Pool(process_number) as p:
        result = p.map_async(function, args)
    delta = datetime.now() - start
    return delta, result


# %%
process_number = 2
args = list(range(6))

start = datetime.now()
with Pool(process_number) as p:
    result = p.map_async(func, args)
    result.wait()
print(result.get())
delta = datetime.now() - start
print(f"Wall time = {delta}")
# %%
list(range(10))
# %%
