from viberbot.api.messages.text_message import TextMessage
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from vars import BotVars

botvars = BotVars()
bot_config = BotConfiguration(
    name=botvars.bot_configs["BOT_NAME"],
    avatar=botvars.bot_configs["BOT_AVATAR"],
    auth_token=botvars.bot_configs["BOT_TOKEN"]
)

viber = Api(bot_config)


def set_hook():
    viber.set_webhook(botvars.bot_configs["BOT_WEBHOOK"])


def bot_message(msg):
    msgtext = TextMessage(text=msg)
    for bot_id in botvars.bot_users.values():
        try:
            viber.send_messages(bot_id, [msgtext])
        except:
            pass


if __name__ == "__main__":
    msg = "Проверка работы Viber!"
    msgtext = TextMessage(text=msg)
    for bot_id in botvars.bot_users.values():
        try:
            viber.send_messages(bot_id, [msgtext])
        except:
            pass
#     # set_hook()