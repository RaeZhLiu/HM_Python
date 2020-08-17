import threading
import time


def sing():
    sing_current_thread = threading.current_thread()
    print("sing_current_thread:", sing_current_thread)
    for i in range(3):
        print("singing....")
        time.sleep(0.3)


def dance():
    dance_current_thread = threading.current_thread()
    print("dance_current_thread:", dance_current_thread)
    for i in range(3):
        print("dancing....")
        time.sleep(0.3)


def main():
    main_current_thread = threading.current_thread()
    print("main_current_thread:", main_current_thread)
    # 1. 创建子线程
    sing_thread = threading.Thread(target=sing, name="sing_thread")
    dance_thread = threading.Thread(target=dance, name="dance_thread")
    # 2. 启动子线程
    sing_thread.start()
    dance_thread.start()


if __name__ == '__main__':
    main()
