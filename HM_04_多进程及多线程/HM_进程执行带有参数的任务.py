import multiprocessing


def show_info(name, age):
    print(name, age)


def main():
    # 1. 创建子进程，以元组方式传参, 以字典方式传参
    sub_process_tuple = multiprocessing.Process(target=show_info, args=("李四", 20))
    sub_process_dic = multiprocessing.Process(target=show_info, kwargs={"age": 20, "name": "李四"})

    sub_process_tuple.start()
    sub_process_dic.start()


if __name__ == '__main__':
    main()
