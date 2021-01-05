def config_name(name):
    # 1. 定义内部函数
    def say_info(message):
        # 2. 内部函数使用外部函数变量
        print(name + ':' + message)
    # 3. 外部函数返回内部函数
    return say_info


zhang_san = config_name("张三")
li_si = config_name("李四")

zhang_san("到北京了吗?")
li_si("到了，请放心！")
