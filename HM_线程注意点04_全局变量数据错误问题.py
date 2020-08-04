import threading

g_value = 0


def f1():
    global g_value
    for i in range(1000000):
        g_value += 1
    print(g_value)


def f2():
    global g_value
    for i in range(1000000):
        g_value += 1
    print(g_value)


def main():
    global g_value
    f1_thread = threading.Thread(target=f1)
    f2_thread = threading.Thread(target=f2)

    f1_thread.start()
    # 方式一：线程等待
    f1_thread.join()
    f2_thread.start()

    print(g_value)


if __name__ == '__main__':
    main()
