import threading


def show_info(name, age):
    print("name:%s, age:%d" % (name, age))


def main():
    # 创建传参数的子线程，以元祖方式传：args，以字典方式传：kwargs
    sub_thread_t = threading.Thread(target=show_info, args=("李四", 18))
    sub_thread_d = threading.Thread(target=show_info, kwargs={"name": "张三", "age": 30})
    # 启动线程
    sub_thread_t.start()
    sub_thread_d.start()


if __name__ == '__main__':
    main()
