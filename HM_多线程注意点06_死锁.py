import threading
# 1.创建互斥锁
mutex = threading.Lock()


def get_value(index):
    mutex.acquire()
    my_list = [1, 5, 1, 4, 6]

    if index >= len(my_list):
        print("下标越界:", index)
        # 越界需要释放互斥锁
        mutex.release()
        return

    # 根据下标取值
    value = my_list[index]
    print(value)
    mutex.release()


def main():
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i, ))
        sub_thread.start()


if __name__ == '__main__':
    main()
