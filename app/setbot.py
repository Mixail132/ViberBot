from config import viber, bot_vars


def set_hook():
    viber.set_webhook(bot_vars.bot_configs["BOT_WEBHOOK"])


def unset_hook():
    viber.unset_webhook()


if __name__ == "__main__":
    set_hook()
