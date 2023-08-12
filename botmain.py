from src.clientConnect import Connect

if __name__ == "__main__":
    #对象
    c = Connect()
    c.connectListent('ws://127.0.0.1:8080')