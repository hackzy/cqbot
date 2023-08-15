import websockets
import asyncio
from src.message import Message
from src.userData import user
#类
class Connect:
    
    async def startConnect(self,uri):
        async with websockets.connect(uri) as self.websocket:
            while True:
                try:
                    message = await self.websocket.recv()  # 接收来自服务器的消息
                    print("收到消息:", message)
                    asyncio.create_task(self.information(message))
                    await self.information(message)
                except websockets.ConnectionClosed:
                    print("连接中断，尝试重连...")
                    await asyncio.sleep(3)  # 等待一段时间后重连

    def connectListent(self,uri):
        asyncio.run(self.startConnect(uri))

    async def information(self,message):
        msg = Message(message,self)
        if msg.postType == 'message':
            await msg.msgAsRead()
            if msg.message == '签到':
                u = user(self)
                ms = u.checkIn(msg.sender)
                await msg.reply(ms)

            

    async def send_ms(self,ms):
        await self.websocket.send(ms)
        

