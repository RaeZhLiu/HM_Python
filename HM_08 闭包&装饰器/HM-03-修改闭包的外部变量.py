def fun_out(a):
    def fun_inner(b):

        nonlocal a  # 通知解释器 此处使用的是外部变量
        a = 10
        result = a + b
        print(result)

    print(a)
    fun_inner(1)
    print(a)

    return fun_inner


f = fun_out(1)
f(2)
f(3)
