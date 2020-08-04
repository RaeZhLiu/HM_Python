import threading
import time


def task():
    time.sleep(0.3)
    # 获取当前线程
    print(threading.current_thread())


def main():
    # 循环创建大量线程，测试线程之间执行是否无序: 线程(进程)之间执行是无序的，由cpu调度线程决定，由操作系统调度进程决定
    for i in range(20):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()


if __name__ == '__main__':
    main()
