import socket

# 创建socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取主机IP，并创建一个端口号
host = socket.gethostname()
port = 10000

# 将host和port绑定并连接
clientSocket.connect((host, port))
print(clientSocket.recv(1024).decode('utf-8'))

clientSocket.send(bytes('D:\\StudyAndWork\\GitRepository\\RecognitionModel\\test3.jpg', 'utf-8'))

print(clientSocket.recv(1024).decode('utf-8'))

clientSocket.close()
