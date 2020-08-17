import socket
import threading
import sys


class HttpWebServer(object):
    def __init__(self, port):
        # 1. 创建 socket 套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定端口
        tcp_server_socket.bind(("", port))
        # 3. 创建监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_connect(request_tcp_socket):
        recv_data = request_tcp_socket.recv(4096)
        print("请求数据为：", recv_data)
        recv_content = recv_data.decode("utf-8")
        # 判断接收的数据长度是否为0
        if len(recv_content) == 0:
            request_tcp_socket.close()
            return

        recv_list = recv_content.split(" ", maxsplit=2)
        request_path = recv_list[1]
        print("请求文件名：", request_path)

        if request_path == "/":
            request_path = "/index.html"

        # os.path.exists("static" + request_path)
        # noinspection PyBroadException
        try:
            # 5. 只读方式打开文件
            with open("static" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            # 6. 拼装异常响应报文
            # 6.1 响应行
            response_line = "HTTP/1.1 404 Not Found \r\n"
            # 6.2 响应头+ 空行
            response_header = "Server:PWS/1.0 \r\n"
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            # 6.3 响应体
            response_body = file_data
            # 6.4 组合
            response_data = (response_line + response_header + '\r\n').encode("utf-8") + response_body
            print("响应数据为：", response_data)

            # 8. 发送响应报文
            request_tcp_socket.send(response_data)
        else:
            # 6. 拼装响应报文
            # 6.1 响应行
            response_line = "HTTP/1.1 200 OK \r\n"
            # 6.2 响应头+ 空行
            response_header = "Server:PWS/1.0 \r\n"
            # 6.3 响应体
            response_body = file_data
            # 6.4 组合
            response_data = (response_line + response_header + '\r\n').encode("utf-8") + response_body
            print("响应数据为：", response_data)

            # 8. 发送响应报文
            request_tcp_socket.send(response_data)
        finally:
            request_tcp_socket.close()

    def start(self):
        # 4. 接受连接
        while True:
            # 4. 接收连接请求，并解码
            request_tcp_socket, ip_port = self.tcp_server_socket.accept()
            connect_thread = threading.Thread(target=self.handle_connect, args=(request_tcp_socket,))
            # 设置守护主线程
            connect_thread.setDaemon(True)
            # 启动子线程
            connect_thread.start()


def main():
    # 获取终端命令行参数
    params = sys.argv
    if len(params) != 2:
        print("命令格式如下：python3 xxx 9000")
        return

    # 判断第二个参数是否都是由数字组成的字符串
    if not params[1].isdigit():
        print("命令格式如下：python3 xxx 9000")
        return

    port = int(params[1])

    # 创建web服务器
    web_server = HttpWebServer(port)
    # 启动服务器
    web_server.start()


if __name__ == '__main__':
    main()
