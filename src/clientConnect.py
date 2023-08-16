import websockets
import asyncio

#类
class Connect:
    
    async def startConnect(self,uri,cqbot):
        async with websockets.connect(uri) as self.websocket:
            cqbot.socket = self.websocket
            while True:
                try:
                    message = await self.websocket.recv()  # 接收来自服务器的消息
                    print("收到消息:", message)
                    asyncio.create_task(cqbot.information(message))
                except websockets.ConnectionClosed:
                    print("连接中断，尝试重连...")
                    await asyncio.sleep(3)  # 等待一段时间后重连

    def connectListent(self,uri,cqbot) :
        asyncio.run(self.startConnect(uri,cqbot))


