import socket
import predict_image

# 创建socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取主机IP，并创建一个端口号
host = socket.gethostname()
port = 10000

# 将host和port绑定
serverSocket.bind((host, port))
# 设置最大连接数为1
serverSocket.listen(5)

print('Server地址为:%s' % str(serverSocket.getsockname()))

while True:
    clientSocket, addr = serverSocket.accept()
    print('连接来自：{}'.format(addr))

    imageName = ''
    # 循环接收消息
    while True:
        # 每次循环接收100字节信息
        recv = clientSocket.recv(100)
        # 解码
        imageName += recv.decode("utf-8")
        # 若以over结尾，则说明消息发送完毕
        if imageName.strip().endswith('over'):
            imageName = imageName[:-4]
            break
    print(imageName)

    result = predict_image.predict_image(imageName)
    clientSocket.send(bytes('%s' % str(result), 'utf-8'))
    clientSocket.close()

    if not imageName:
        break

serverSocket.close()
