import multiprocessing
import time
import os


# 跳舞任务
def dance():
    # 获取当前进程的编号
    dance_process_id = os.getpid()
    print("dance_process_id:", dance_process_id, multiprocessing.current_process())
    # 获取当前进程的父进程编号 os.getppid()
    dance_process_parent_id = os.getppid()
    print("dance_process的父进程编号是：", dance_process_parent_id)
    for i in range(3):
        print("dancing....")
        time.sleep(0.1)
        # 根据进程编号强制杀死进程
        os.kill(dance_process_id, 9)


def sing():
    # 获取当前进程的编号
    sing_process_id = os.getpid()
    print("sing_process_id:", sing_process_id, multiprocessing.current_process())
    # 获取当前进程的父进程编号 os.getppid()
    sing_process_parent_id = os.getppid()
    print("sing_process的父进程编号是：", sing_process_parent_id)
    for i in range(3):
        print("singing....")
        time.sleep(0.1)


def main():
    # 获取当前进程的编号 os.getpid()
    main_process_id = os.getpid()
    print("main_process_id:", main_process_id, multiprocessing.current_process())

    # 1. 创建子进程
    # 1.1. group表示进程组，目前仅能使用None，一般不需要设置
    # 1.2. target表示进程执行的目标任务
    # 1.3. name表示进程名，默认为Processing-1,....
    dance_process = multiprocessing.Process(target=dance)
    print("dance_process:", dance_process)
    sing_process = multiprocessing.Process(target=sing)
    print("sing_process:", sing_process)
    # 2. 启动子进程, 进程执行是无序的，取决于cpu调度®
    dance_process.start()
    sing_process.start()
    # 主进程执行对应的任务
    # sing()


if __name__ == "__main__":
    main()
