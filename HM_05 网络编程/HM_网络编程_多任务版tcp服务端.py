import socket
import threading


def new_socket(new_t_socket, num):
    while True:
        recv_content = new_t_socket.recv(1024)
        recv_data = recv_content.decode("GBK")
        if len(recv_data) == 0:
            print("客户端 %d 断开连接" % num)
            break
        print("接受 %d 号客户端的数据:%s" % (num, recv_data))
        send_data = "Hi, 你好"
        send_content = send_data.encode("GBK")
        new_t_socket.send(send_content)
    new_t_socket.close()


def main():
    # 1. 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定本机IP及PORT
    tcp_server_socket.bind(("", 9090))
    # 3. listen连接
    tcp_server_socket.listen(128)
    # 4. 接受连接
    # new_socket(new_t_socket)
    for i in range(10):
        new_t_socket, ip_port = tcp_server_socket.accept()
        print("客户端 %d 建立连接成功 %s" % (i+1, ip_port))
        server_thread = threading.Thread(target=new_socket, args=(new_t_socket, i+1))
        server_thread.setDaemon(True)
        server_thread.start()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
