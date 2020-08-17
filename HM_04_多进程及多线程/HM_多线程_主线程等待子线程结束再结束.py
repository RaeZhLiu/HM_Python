import threading
import time


def task():
    while True:
        print("Processing....")
        time.sleep(0.1)


def main():
    # daemon = True表示创建的子线程守护主线程，主线程退出则子线程自动结束
    # sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread = threading.Thread(target=task)
    # 把子线程设置成为守护主线程
    sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print("Over")

    # 主线程会等待子线程执行结束再结束


if __name__ == '__main__':
    main()
