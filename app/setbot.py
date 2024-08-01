from config import viber, botvars


def set_hook():
    viber.set_webhook(botvars.bot_configs["BOT_WEBHOOK"])


if __name__ == "__main__":
    set_hook()
