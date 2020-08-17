import multiprocessing
import time

# 定义全局变量
g_list = list()


# 添加数据
def add_data():
    for i in range(3):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.1)
    print("添加完成：", g_list)


# 读取数据
def read_data():
    print("read:", g_list)


def main():
    # 添加数据子进程
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    #启动进程
    add_process.start()
    # 主进程等待添加数据的子进程执行完再向下执行
    add_process.join()
    read_process.start()
    print("main:", g_list)
    # 结论：进程间不共享全局变量，属于多份copy

if __name__ == "__main__":
    main()
