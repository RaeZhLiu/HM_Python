import socket


def main():
    # 1. 创建tcp服务端套接字
    # 1.1 socket.AF_INET: ipv4  socket.SOCK_STREAM：tcp传输协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定端口号
    # 2.1 元组:第一个参数一般不指定，第二个参数表示端口号
    tcp_server_socket.bind(("", 9090))
    # 3. 设置监听
    # 3.1 128表示最大等待建立连接的个数
    tcp_server_socket.listen(128)
    for i in range(10):
        # 4. 等待接受客户端的连接请求
        # 4.1 会阻塞，等待连接到来，每次建立连接都会返回元组，其中 参数一：新的套接字，参数二：客户端的IP及PORT
        # 4.2 tcp_server_socket只负责等待接收客户端的连接请求，收发消息都不使用该套接字
        new_socket, ip_port = tcp_server_socket.accept()
        # 4.3 代码执行到此，表示客户端与服务端建立连接成功
        print("连接%d号客户端成功，IP及PORT：%s" % (i, ip_port))
        while True:
            # 5. 接收客户端的请求
            recv_data = new_socket.recv(1024)
            # 5.1 对接收的二进制数据解码
            recv_content = recv_data.decode("GBK")
            if len(recv_content) == 0:
                print("断开连接")
                break
            print("接收%d号客户端的数据为：%s" % (i, recv_content))
            # 6. 发送数据到客户端
            send_content = "问题正在处理中....."
            send_data = send_content.encode("GBK")
            new_socket.send(send_data)

        # 7. 关闭套接字
        new_socket.close()
        if i == 9:
            print("服务结束，服务端自动退出")
            break
    # 8. 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
