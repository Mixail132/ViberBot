""" Initial hook settings for the bot. """
from config import viber, bot_vars


def set_hook():
    """ Sets the bot web hook. """
    viber.set_webhook(bot_vars.configs["bot_webhook"])


def unset_hook():
    """ Unsets the bot webhook. """
    viber.unset_webhook()


if __name__ == "__main__":
    set_hook()
