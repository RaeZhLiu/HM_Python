import multiprocessing
import time


def task():
    for i in range(10):
        print("任务执行中....")
        time.sleep(0.2)


def main():
    task_process = multiprocessing.Process(target=task)
    # # 把子进程设置成为守护主进程，即主进程结束，子进程自动销毁
    # task_process.daemon = True
    task_process.start()

    time.sleep(0.5)
    # 主进程结束前，手动销毁子进程
    task_process.terminate()
    print("over")

    # 结论：主进程会等待子进程执行完成以后程序再退出


if __name__ == '__main__':
    main()
