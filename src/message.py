import json
class Message:
    postType = ''
    messageType = ''
    sendId = ''
    groupId = 0
    userId = 0
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
                    self.groupId = loadMessage['group_id']  #-群号
                elif self.messageType == 'private':
                    self.userId = loadMessage['user_id']
                self.messageId = loadMessage['message_id']
                self.subType = loadMessage['sub_type']
                self.message = loadMessage['message']
                self.sender = sender(loadMessage['sender']) #--发送人
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
                        "user_id": self.userId,
                        "group_id":self.groupId,
                        "message":message,
                        "auto_escape":False
            },
            "echo": "test"
        }
        await self.client.send_ms(json.dumps(js))

    async def deleteMsg(self):
        js = {
            "action":'delete_msg',
            'params':{
                'message_id':self.messageId
            }
        }
        await self.client.send_ms(json.dumps(js))

    async def msgAsRead(self):
        js = {
            "action":'mark_msg_as_read',
            'params':{
                'message_id':self.messageId
            },
            'echo':''
        }
        await self.client.send_ms(json.dumps(js))

class sender:
    def __init__(self,sender) -> None:
        self.id = sender['user_id']
        self.name = sender['nickname']