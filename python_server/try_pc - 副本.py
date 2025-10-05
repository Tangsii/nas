import socket
import json

def send_request(param1, param2):
    # 创建TCP/IP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接服务器
    server_address = ('192.168.1.47', 5667)
    print(f"连接到服务器 {server_address}")
    sock.connect(server_address)
    
    try:
        # 发送数据
        message = json.dumps({'param1': param1, 'param2': param2}).encode('utf-8')
        print(f"发送: {message.decode('utf-8')}")
        sock.sendall(message)
        
        # 接收响应
        data = sock.recv(1024)
        print(f"收到: {data.decode('utf-8')}")
        
        # 解析结果
        result = json.loads(data.decode('utf-8'))
        return result['result']
        
    finally:
        # 关闭连接
        sock.close()

# 获取用户输入
param1 = float(input("请输入参数1: "))
param2 = float(input("请输入参数2: "))

# 发送请求并获取结果
result = send_request(param1, param2)
print(f"计算结果: {result}")