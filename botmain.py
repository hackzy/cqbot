from pycqBot import cqHttpApi,cqLog
import logging
import os
if __name__ == '__main__':
    cqLog()
    cqapi = cqHttpApi()
    bot = cqapi.create_bot(group_id_list=[375281736,454661594],options={'commandSign':''})
    bot.plugin_load("myPlugin")
    bot.start(start_go_cqhttp=False)
