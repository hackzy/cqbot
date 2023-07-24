from pycqBot import cqHttpApi,cqLog
import logging
cqLog(logging.INFO)
cqapi = cqHttpApi()
bot = cqapi.create_bot(group_id_list=[375281736,454661594],options={'commandSign':''})
bot.plugin_load("myPlugin")
bot.start(start_go_cqhttp=False)
