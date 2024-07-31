from viberbot.api.messages.text_message import TextMessage
from dotenv import load_dotenv
import os
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

load_dotenv()

viber_webhook = os.getenv("VIBER_WEBHOOK")
viber_botname = os.getenv("VIBER_BOTNAME")
viber_avatar = os.getenv("VIBER_AVATAR")
viber_token = os.getenv("VIBER_TOKEN")

bot_config = BotConfiguration(
    name=viber_botname,
    avatar=viber_avatar,
    auth_token=viber_token
)
viber = Api(bot_config)

def sethook():
    viber.set_webhook(viber_webhook)
#
# def to_viber(msg):
#     msgtext = TextMessage(text=msg)
#     for i in viber_users.values():
#         try:
#             viber.send_messages(i, [msgtext])
#         except:
#             pass
#
#
# if __name__ == "__main__":
#     msg = "Проверка работы Viber!"
#     msgtext = TextMessage(text=msg)
#     for i in viber_users.values():
#         try:
#             viber.send_messages(i, [msgtext])
#         except:
#             pass
#     # sethook()