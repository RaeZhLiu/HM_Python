def func_out(num1):
    # 1. 定义一个内部函数
    def func_inner(num2):
        # 2. 内部函数使用了外部函数的变量
        result = num1 + num2
        print(result)
    # 3. 外部函数返回了内部函数
    return func_inner


# 创建闭包实例
f = func_out(1)
# 执行闭包
f(2)
f(3)
