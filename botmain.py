from pycqBot import cqHttpApi,cqLog
from pycqBot.data import Message
import json
import logging
import os
cqLog(logging.INFO)

cqapi = cqHttpApi()

def getInfo(sender):
    if os.path.exists('./data/'+sender+'.json'):
        with open('./data/'+sender+'.json') as file:
            data = json.load(file)
            file.close()
            days = int(data['签到']) + 1
            return str(days)
    savedata = {'签到':1}
    with open('./data/'+sender+'.json','w') as file:
        json.dump(savedata,file,ensure_ascii=False,indent=2)
        file.close()
        return str(1)



bot = cqapi.create_bot(group_id_list=[375281736,454661594],options={'commandSign':''})
bot.plugin_load(["myPlugin"])


bot.start(start_go_cqhttp=False)