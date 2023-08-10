import json
import asyncio
class Message:
    postType = ''
    messageType = ''
    sendId = ''
    
    def __init__(self,message:str,client) -> None:
        self.client = client
        loadMessage = json.loads(message)
        '''主消息类型'''
        try:
            self.postType = loadMessage['post_type']
            '''子消息类型'''
            if self.postType == 'message':
                self.messageType = loadMessage['message_type']
                if self.messageType == 'group':
                    self.sendId = loadMessage['group_id']  #-群号
                elif self.messageType == 'private':
                    self.sendId = loadMessage['user_id']
                self.subType = loadMessage['sub_type']
                self.message = loadMessage['message']
                self.sender = loadMessage['sender'] #--发送人
            elif self.postType == 'meta_event':
                self.metaEventType = loadMessage['meta_event_type']
            self.botId = loadMessage['self_id']
        except KeyError:
            print(loadMessage)

    async def reply(self,message:str):
        
        js = {
            "action": 'send_msg',
            "params": {
                        "message_type": self.messageType,
                        "user_id": self.sendId,
                        "message":message,
                        "auto_escape":False
            },
            "echo": "test"
        }
        await self.client.send_ms(json.dumps(js))