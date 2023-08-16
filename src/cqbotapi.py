import json
import sqlite3
from src.clientConnect import Connect
import websockets
from src.message import Message
from src.userData import user
class bot:
    def __init__(self,uri) -> None:
        with open('data/data.json','r',encoding='utf8') as file:
            loadjs = json.load(file)
        self.blackList = loadjs['black']
        self.questionList = loadjs['question']
        self.keyword = loadjs['keyword']
        self.serviceGroup = loadjs['Group']
        c = Connect()
        self.socket = c.connectListent(uri,self)

    async def information(self,message):
        msg = Message(message,self)
        if msg.postType == 'message':
            await msg.msgAsRead()
            ms = self.msgProcess(msg)
            if msg.message == '签到':
                u = user(self)
                ms = u.checkIn(msg.sender)
            if ms != '':
                await msg.reply(ms)

    def __findBlackKeyWord(self,ms:str):
        for b in self.keyword:
            if ms.find(b) != -1:
                return True

    def msgProcess(self,ms:Message):
        if ms.message == '签到':
            u = user(self)
            ms = u.checkIn(ms.sender)
        elif self.__findBlackKeyWord(ms.message):
            ms.deleteMsg()
            ms = ''
        return ms
            
    async def send(self,ms):
        await self.socket.send(ms)
        

