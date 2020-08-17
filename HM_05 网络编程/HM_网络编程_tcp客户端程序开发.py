import socket


def main():
    # 1. 创建tcp客户端套接字
    # AF.INET: 表示ipv4的地址类型
    # SOCK_STREAM: 表示tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 和服务端套接字建立连接
    tcp_client_socket.connect(("10.156.4.115", 9999))
    # 3. 发送数据到服务端
    # 3.1 将字符串转换成二进制
    send_content = "你好，我是客户端小白！！"
    send_data = send_content.encode("GBK")
    tcp_client_socket.send(send_data)
    # 4. 接收服务端的数据
    # 4.1 1024表示每次接收的最大字节数
    recv_data = tcp_client_socket.recv(1024)
    # 4.2 对二进制数据进行解码
    recv_content = recv_data.decode("GBK")
    print("接收服务端的数据为：", recv_content)
    # 5. 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
