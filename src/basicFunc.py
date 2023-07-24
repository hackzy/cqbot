# src\basicFunc.py
import requests
def getAvatar(qq):
    return '[CQ:image,file=https://tenapi.cn/v2/qqimg?qq=%s]'%(str(qq))

def getLevel(qq):
    json = requests.get('https://api.uomg.com/api/get.qqdj?qq=%s&skey=@surhcc2'%(str(qq)))
    print(json.text)