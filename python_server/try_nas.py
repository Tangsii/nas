import socket
import json
import time

# 模拟耗时计算
def calculate(param1, param2):
    print(f"开始计算: {param1}, {param2}")
    time.sleep(5)  # 模拟耗时计算
    result = param1 * param2
    print(f"计算完成: {result}")  # 确认计算结果
    return result

# 创建TCP/IP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 5668)
print(f"服务器启动，监听 {server_address}")
sock.bind(server_address)
sock.listen(1)

while True:
    print("等待连接...")
    connection, client_address = sock.accept()
    try:
        print(f"连接来自 {client_address}")
        
        # 接收数据
        data = connection.recv(1024)
        if data:
            # 新增：打印收到的原始数据（确认客户端发送是否正常）
            print(f"收到客户端原始数据: {data.decode('utf-8')}")
            # 解析JSON数据
            params = json.loads(data.decode('utf-8'))
            print(f"解析后参数: {params}")
            
            # 执行计算
            result = calculate(params['param1'], params['param2'])
            
            # 准备返回结果（新增：打印要发送的JSON）
            response_json = json.dumps({'result': result})
            print(f"准备发送的JSON结果: {response_json}")  # 关键：确认JSON格式是否正确
            response = response_json.encode('utf-8')
            connection.sendall(response)
            print(f"结果已发送: {response}")  # 确认是否发送成功
        else:
            print("未收到数据")
    except Exception as e:
        # 新增：捕获服务器端所有异常并打印（关键！排查是否有隐性错误）
        print(f"服务器处理请求时出错: {str(e)}")
    finally:
        connection.close()
        print("连接已关闭\n")  # 分隔每次请求的日志