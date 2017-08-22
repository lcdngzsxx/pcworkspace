import time
import concurrent.futures

numers = list(range(1, 11))


# caculate dense
def count(n):
    for i in range(100000000):
        i += i
    return i * n


def worker(x):
    result = count(x)
    print(f'num {x} caculate result:{result}')


def sequential_execution():
    star_time = time.clock()
    for i in numers:
        worker(i)
    print(f'sequential_execution consuming time:{time.clock()-star_time}')


def threading_exection():
    star_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as excutor:
        for i in numers:
            excutor.submit(worker, i)
    print(f'threadingpool consuming time :{time.clock()-star_time}')


def process_excution():
    start_time = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as excutor:
        for i in numers:
            excutor.submit(worker, i)
    print(f'process_excution consuming time: {time.clock()-start_time}')


if __name__ == '__main__':
    process_excution()
    
# 测试forlk    
