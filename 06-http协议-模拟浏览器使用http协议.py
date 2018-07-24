# # 需求: 使用一个python文件,模拟浏览器的形式访问www.baidu.com
# #   思路1: 创建一个tcp客户端,主动链接www.baidu.com,80端口
# #   思路2: 链接成功后,发送一个请求;(请求行+请求头+空行)
# #   思路3: 请求发送完毕,就可以接收数据;(长连接 -- 保存到一个文件中)
# import socket
#
# if __name__ == '__main__':
#     #  思路1: 创建一个tcp客户端,主动链接www.baidu.com,80端口
#     tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 加www和不加w是连接两个不同的服务器
#     ip_port = ('www.baidu.com', 80)
#     tcp_socket.connect(ip_port)
#
#     #   思路2: 链接成功后,发送一个请求;(请求行+请求头+空行)
#     request_line = 'GET / HTTP/1.1\r\n'
#     request_header = 'Host: www.baidu.com\r\n'
#     request_data = request_line + request_header + '\r\n'
#     # 请求报文: 行和头部分拼好后,编码成二进制
#     tcp_socket.send(request_data.encode('utf-8'))
#
#     #   思路3: 请求发送完毕,就可以接收数据;(长连接 -- 保存到一个文件中)
#     data_bin = tcp_socket.recv(5000)
#     print(data_bin)
#     print(data_bin.decode())
#
#     # 写入的时候,不能写入响应头和响应行
#     response_list = data_bin.decode().split('\r\n\r\n')
#     response_body = response_list[1]
#     print(response_body)
#
#     # 创建文件,直接写入
#     # 这里曾经
#     with open('download/baidu.html', 'wb') as file:
#         file.write(response_body.encode())
#         # # 为了确保对方发送的是长连接,这个位置还要继续接收!(死循环接收)
#         while True:
#             data_bin2 = tcp_socket.recv(5000)
#             # 这时候获取的内容就没有响应头,响应行了,只剩响应体了...
#             if data_bin2:
#                 file.write(data_bin2)
#             else:
#                 break
#
#     tcp_socket.close()

# import socket
#
#
# #   思路1: 创建一个tcp客户端,主动链接www.baidu.com,80端口
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 加www和不加w是连接两个不同的服务器
# ip_port = ('www.baidu.com', 80)
# tcp_socket.connect(ip_port)
#
# #   思路2: 链接成功后,发送一个请求;(请求行+请求头+空行)
# request_line = 'GET / HTTP/1.1\r\n'
# request_header = 'Host: www.baidu.com\r\n'
# request_data = request_line + request_header + '\r\n'
# # 请求报文: 行和头部分拼好后,编码成二进制
# tcp_socket.send(request_data.encode('utf-8'))
#
# #   思路3: 请求发送完毕,就可以接收数据;(长连接 -- 保存到一个文件中)
# data_bin = tcp_socket.recv(5000)
# print(data_bin)
# print(data_bin.decode())
#
# # 写入的时候,不能写入响应头和响应行
# response_list = data_bin.decode().split('\r\n\r\n')
# response_body = response_list[1]
# print(response_body)
#
# # 创建文件,直接写入
# # 这里曾经
# with open('download/baidu.html', 'wb') as file:
#     file.write(response_body.encode())
#     # 为了确保对方发送的是长连接,这个位置还要继续接收!(死循环接收)
#     while True:
#         data_bin2 = tcp_socket.recv(5000)
#         # 这时候获取的内容就没有响应头,响应行了,只剩响应体了...
#         if data_bin2:
#             file.write(data_bin2)
#         else:
#             break
#
# tcp_socket.close()

# import socket
#
# # 1.创建一个tcp客户端，主动链接www.baidu.com,80 端口
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_socket.connect(('www.baidu.com', 80))
#
# # 2.创建成功后，发送一个请求；
# # 请求行+请求头+空头
# # 请求报文：行和头部分拼好，编码成二进制，
# request_data = 'GET / HTTP/1.1\r\n' + 'Host: www.baidu.com\r\n' + '\r\n'
# tcp_socket.send(request_data.encode('utf-8'))
#
# # 3.请求发送完毕，就可以接受数据（长链接--保存到一个文件中）
# # 写入的时候，不能写入响应头和响应行
# response_list = tcp_socket.recv(5000).decode().split('\r\n\r\n')
# response_body = response_list[1]
#
# # 创建文件，直接写入
# # 这里曾经我尝试使用'w'来直接写入，后来发现子啊rec(5000)那里，5000决定了它解码的位置，难以判断，故而舍弃
# with open('download/baidu.html', 'wb') as file:
#     file.write(response_body.encode())
#     # 为了确保对方发送的是长链接，这个位置还要继续接受！(死循环接收)
#     while True:
#         data_bin_loop = tcp_socket.recv(5000)
#         # 这时候获取的内容就没有响应头，响应行了，只剩响应体....
#         if data_bin_loop:
#             file.write(data_bin_loop)
#         else:
#             break
# tcp_socket.close()
# import socket
# # 1：创建一个tcp客户端，链接www.baidu.com,80端口
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_socket.connect(('https://www.cnblogs.com', 80))
#
# # 我换了网站，博哥认为这就相当于一个爬虫，很多网站需要你验证各种东西。
# # 2: 链接成功后，发送一个请求；（请求行，请求头 + 空行）
# response_line = 'GET / HTTP/1.1\r\n'
# response_header = 'Host: www.cnblogs.com\r\n'
# request_data = response_line + response_header + '\r\n'
# # 拼接好之后，编制成二进制，请求报文
# tcp_socket.send(request_data.encode('utf-8'))
#
# # 3: 请求发送完毕，就可以接收到报文；（长链接 -- 保存到一个文件中）
# data_bin = tcp_socket.recv(5000).decode().split('\r\n\r\n')
# response_body = data_bin[1]
#
# with open('download/baidu.html', 'wb') as file:
#     file.write(response_body.encode())
#     while True:
#         data_loop = tcp_socket.recv(5000)
#         if data_loop:
#             file.write(data_loop)
#         else:
#             break
# tcp_socket.close()

#