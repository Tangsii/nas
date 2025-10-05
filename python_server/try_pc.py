import socket
import json

def send_tcp_request(param1, param2, server_ip='192.168.1.47', server_port=5668):
    # 创建TCP Socket客户端
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 连接到服务器
        client_socket.connect((server_ip, server_port))
        print(f"成功连接到服务器 ({server_ip}, {server_port})")
        
        # 准备参数（转为JSON字符串并编码为字节流）
        params = {"param1": param1, "param2": param2}
        send_data = json.dumps(params).encode('utf-8')
        print(f"发送参数: {params}")
        client_socket.sendall(send_data)
        
        # 接收服务器返回的结果（缓冲区1024字节，可根据结果大小调整）
        print("等待服务器计算结果...")
        recv_data = client_socket.recv(1024)
        
        if recv_data:
            # 解析服务器返回的JSON结果
            result = json.loads(recv_data.decode('utf-8'))
            print(f"计算完成，服务器返回结果: {result['result']}")
            return result['result']
        else:
            print("未收到服务器返回数据")
            return None
    
    except ConnectionRefusedError:
        print("连接失败：无法连接到服务器，请检查服务器IP、端口是否正确，或服务器是否已启动")
        return None
    except json.JSONDecodeError:
        print("数据解析错误：服务器返回的不是有效的JSON格式")
        return None
    except Exception as e:
        print(f"请求过程中发生错误: {str(e)}")
        return None
    finally:
        # 关闭客户端Socket连接
        client_socket.close()
        print("客户端连接已关闭")

if __name__ == "__main__":
    # 获取用户输入的参数（支持整数/浮点数）
    try:
        param1 = float(input("请输入参数1: "))
        param2 = float(input("请输入参数2: "))
        
        # 调用函数发送请求并获取结果
        send_tcp_request(param1, param2)
    
    except ValueError:
        print("输入错误：请输入有效的数字（整数或小数）")