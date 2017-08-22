import multiprocessing
import time
'''mulitprocessing 充分运用多核，多CPU的计算能力，适用于计算密集型任务
'''
def func(n):
    print(f'{multiprocessing.current_process().name} func start:{time.ctime()}')
    time.sleep(n)
    print(f'{multiprocessing.current_process().name} func end:{time.ctime()}')

def main():
    print(f'main run start:{time.ctime()}')
    processes =[]
    p1 = multiprocessing.Process(target=func,args=(4,))
    processes.append(p1)
    p2 = multiprocessing.Process(target=func , args=(2 ,))
    processes.append(p2)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f'main run end:{time.ctime()}')

if __name__ == '__main__':
    main()