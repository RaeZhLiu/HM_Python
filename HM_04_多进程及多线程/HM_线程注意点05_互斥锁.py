import threading

# 1.创建全局变量
g_value = 0
# 2. 创建互斥锁，Lock本质上是一个函数，可以创建一个互斥锁对象
lock = threading.Lock()


def f1():
    # 上锁
    lock.acquire()
    global g_value
    for i in range(1000000):
        g_value += 1
    print(g_value)
    # 释放锁
    lock.release()


def f2():
    # 上锁,若有别的线程已上锁，则等待
    lock.acquire()
    global g_value
    for i in range(1000000):
        g_value += 1
    print(g_value)
    # 释放锁
    lock.release()


def main():
    global g_value
    f1_thread = threading.Thread(target=f1)
    f2_thread = threading.Thread(target=f2)

    f1_thread.start()
    f2_thread.start()

    print(g_value)
    # 互斥锁可以保证同一时刻只有一个线程去执行代码，能够保证全局变量的结果没有问题，保证数据安全，但执行效率下降
    # 线程等待和互斥锁都是把多认为改成单任务去执行，保证数据准确性，但执行性能会下降


if __name__ == '__main__':
    main()
