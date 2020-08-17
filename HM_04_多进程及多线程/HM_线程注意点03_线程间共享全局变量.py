import threading
import time

value = list()


def add():
    for i in range(3):
        print("添加数据：", i)
        value.append(i)
        time.sleep(0.1)

    print("添加数据完成：", value)


def show():
    print("显示列表：", value)


def main():
    add_thread = threading.Thread(target=add)
    show_thread = threading.Thread(target=show)

    add_thread.start()
    # 等待add线程执行完再执行后续代码
    add_thread.join()

    show_thread.start()


if __name__ == '__main__':
    main()
