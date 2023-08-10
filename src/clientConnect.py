import websockets
import asyncio
from message import Message
#类
class Connect:
    
    async def startConnect(self,uri):
        async with websockets.connect(uri) as self.websocket:
            while True:
                try:
                    message = await self.websocket.recv()  # 接收来自服务器的消息
                    print("收到消息:", message)
                    await self.information(message)
                except websockets.ConnectionClosed:
                    print("连接中断，尝试重连...")
                    await asyncio.sleep(3)  # 等待一段时间后重连

    def connectListent(self):
        asyncio.get_event_loop().run_until_complete(c.startConnect('ws://127.0.0.1:8080',))

    async def information(self,message):
        ms = Message(message,self)
        if ms.postType == 'message':
            await ms.reply('发送测试')
            

    async def send_ms(self,ms):
        await self.websocket.send(ms)
        
if __name__ == "__main__":
    #对象
    c = Connect()
    c.connectListent()
#收到消息: {"post_type":"message","message_type":"private","time":1691582735,"self_id":1755203518,"sub_type":"friend","user_id":959683906,"target_id":1755203518,"message":"签到","raw_message":"签
#到","font":0,"sender":{"age":0,"nickname":"hackzy","sex":"unknown","user_id":959683906},"message_id":-419633169}
'''收到消息: {"post_type":"message","message_type":"group","time":1691582769,"self_id":1755203518,"sub_type":"normal","font":0,"group_id":454661594,"sender":{"age":0,"area":"","card":"","level":"","nickname":"hackzy","role":"owner","sex":"unknown","title":"","user_id":959683906},"anonymous":null,"message":"签到","message_seq":36417,"raw_message":"签到","user_id":959683906,"message_id":-1304542928}'''