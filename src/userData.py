import json
import os
from src.basicFunc import *
import random
class user:
    def __init__(self,plugin) -> None:
        self.plugin = plugin
        
    def getInfo(self,sender):
        if os.path.exists('./data/' + str(sender.id) + '.json'):
            with open('./data/' + str(sender.id) + '.json','r',encoding='utf8') as file:
                data = json.load(file)
                file.close()
                self.days = int(data['累计天数']) 
                self.points = int(data['积分'])
        else:
            self.days = 0
            self.points = 0

    def saveInfo(self,sender):
        saveData = {
            '累计天数':self.days,
            '积分':self.points
        }
        with open('./data/' + str(sender.id) + '.json','w',encoding='utf8') as file:
            json.dump(saveData,file,ensure_ascii=False,indent=2)
            file.close()
            
    def checkIn(self,sender):
        if sender.id not in self.plugin.checkIns:
            self.getInfo(sender)
            self.days += 1
            addPoints = random.randint(1,10)
            self.points += addPoints
            self.plugin.checkIns.append(sender.id)
            self.saveInfo(sender)
            message = getAvatar(sender.id) + '\n'
            message += '🆔' + sender.nickname + '\n'
            message += '🔔签到成功！\n'
            message += '🌟累计签到' + str(self.days) + '天\n'
            message += '🌟本次签到获得积分：' + str(addPoints) + '\n'
            message += '🌟当前拥有积分：' + str(self.points)
        else:
            message = '你今天已签到了哦！请不要重复签到！'
        return message


