#from pycqBot.cqApi import cqBot, cqHttpApi
from pycqBot.object import Plugin
from pycqBot.data import *

class myPlugin(Plugin):

    def __init__(self, bot, cqapi, plugin_config):
        super().__init__(bot, cqapi, plugin_config)
        #self.text = plugin_config["text"]
        bot.command(self.test_plugin, "test", {
            "type": "all"
        })
    
    def test_plugin(self,commed,message:Message):
        message.reply_not_code(str(message.sender.id)+'\n'+message.sender.card+'\n'+message.sender.level\
                               +'\n'+message.sender.nickname)