from viberbot.api.messages.text_message import TextMessage
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from vars import BotVars

bot_vars = BotVars()
bot_config = BotConfiguration(
    name=bot_vars.configs["bot_name"],
    avatar=bot_vars.configs["bot_avatar"],
    auth_token=bot_vars.configs["bot_token"]
)

viber = Api(bot_config)


def bot_message(messg):
    msg_text = TextMessage(text=messg)
    for bot_id in bot_vars.users.values():
        try:
            viber.send_messages(bot_id, [msg_text])
        except:
            pass


if __name__ == "__main__":
    msg = "Проверка работы Viber!"
    msgtext = TextMessage(text=msg)
    for sender_id in bot_vars.users.values():
        try:
            viber.send_messages(sender_id, [msgtext])
        except:
            pass
