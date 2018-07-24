# 需求: 写一个tcp的服务端,客户端用普通浏览器访问我们的服务端,看看收到的是什么样的格式信息...
import socket

if __name__ == '__main__':
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.服务端应该绑定端口
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tuple1 = ('192.168.44.128', 9999)
    tcp_socket.bind(tuple1)
    # 3.变主动为被动
    tcp_socket.listen(128)
    # 4.死循环接收客户端发送的链接请求
    while True:
        print('服务器以开启,等待客户端链接...')
        service_client_socket, ip_port = tcp_socket.accept()
        print(ip_port, "已连接...")
        # 5.接收来着客户端的信息...
        str1 = service_client_socket.recv(5000)
        print('二进制代码: ', str1)
        print('转换后代码: ', str1.decode())
        # 不回复任何信息,因为我们就是向看看格式...
        # 6.关闭套接字
        service_client_socket.close()


# 二进制代码:
#    b'GET / HTTP/1.1\r\nHost: 192.168.44.128:9999\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'


# 转换后代码:
# GET / HTTP/1.1
# Host: 192.168.44.128:9999
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9


