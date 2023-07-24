#plugin/myPlugin/myPlugin.py
from pycqBot.object import Plugin
from pycqBot.data import *

class myPlugin(Plugin):
    def __init__(self, bot, cqapi, plugin_config):
        super().__init__(bot, cqapi, plugin_config)
        #self.text = plugin_config["text"]
        bot.command(self.usr_checkin, "签到", {
            "type": "all"
        })
    
    def usr_checkin(self,commed,message:Message):
        from src.userData import user
        u = user(self)
        ms = u.checkIn(message.sender)
        message.reply_not_code(ms)
        