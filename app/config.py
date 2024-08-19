""" The bot configuration settings. """

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


if __name__ == "__main__":
    msg = TextMessage(text="Checking the Viber Bot!")
    sender_id = bot_vars.users["admin"]
    viber.send_messages(sender_id, [msg])
