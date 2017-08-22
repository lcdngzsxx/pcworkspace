import threading
import queue
import time
import random

def producer(data_queue):
    for i in range(5):
        time.sleep(0.5)
        item = random.randint(1,100)
        data_queue.put(item)
        print(f'{threading.current_thread().name} put in :{item}')

def consumer(data_queue):
    while True:
        try:
            item = data_queue.get(timeout=3)
            print(f'{threading.current_thread().name} get out :{item}')
        except queue.Empty:
            print('queue is empty')
            break
        else:
            data_queue.task_done()

def main():
    q = queue.Queue()
    threads = []
    p = threading.Thread(target=producer,args=(q,))
    p.start()

    for i in range(12):
        c = threading.Thread(target=consumer,args=(q,))
        threads.append(c)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    q.join()

if __name__ == '__main__':
    main()