import json
import os
from .basicFunc import *
import random
from datetime import datetime
import threading
class user:
    def __init__(self,plugin) -> None:
        self.plugin = plugin
        self.checkIns = {}
        
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
            
    def getCheckIns(self,days):
        if os.path.exists(os.getcwd() + '/data/checkin.json'):
            with open(os.getcwd() + '/data/checkin.json','r',encoding='utf8') as file:
                self.checkIns = json.load(file)
                if days not in self.checkIns:
                    self.checkIns = {days:[]}
        else:
            self.setCheckIns()
    def setCheckIns(self):
        with open(os.getcwd() + '/data/checkin.json','w',encoding='utf8') as file:
            json.dump(self.checkIns,file,ensure_ascii=False,indent=2)

    def checkIn(self,sender):
        date = datetime.now()
        days = str(date.month) + '.' + str(date.day)
        self.getCheckIns(days)
        if sender.id not in self.checkIns[days]:
            self.getInfo(sender)
            self.days += 1
            addPoints = random.randint(1,10)
            self.points += addPoints
            self.checkIns[days].append(sender.id)
            self.setCheckIns()
            self.saveInfo(sender)
            cq_at = '[CQ:at,qq=%s]'%(sender.id)
            message = getAvatar(sender.id) + '\n'
            message += '🆔' + cq_at + '\n'
            message += '🔔签到成功！\n'
            message += '🌟累计签到' + str(self.days) + '天\n'
            message += '🌟本次签到获得积分：' + str(addPoints) + '\n'
            message += '🌟当前拥有积分：' + str(self.points)
        else:
            message = '你今天已签到了哦,请不要重复签到！'
        return message
    
    def resetCheckIns(self):
        with open('./data/checkin.json','w',encoding='utf8') as file:
            self.checkIns = {}
            json.dump(self.checkIns,file,ensure_ascii=False,indent=2)
            task = threading.Timer(self.getTime(),self.resetCheckIns)
            task.daemon = True
            task.start()

    def getTime(self):
        nowtime = datetime.datetime.now()
        now = datetime.timedelta(hours=nowtime.hour,minutes=nowtime.minute,seconds=nowtime.second,microseconds=nowtime.microsecond)
        rangeSecond = datetime.timedelta(hours=24,minutes=00,seconds=00) - now
        return rangeSecond


    def daysTask(self):
        task = threading.Timer(self.getTime(),self.resetCheckIns)
        task.daemon = True
        task.start()