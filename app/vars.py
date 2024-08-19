""" The configuration variables reading and setting. """

import configparser
from pathlib import Path


class IniSection(configparser.ConfigParser):
    """ Returns the built in method as a simple method. """
    @property
    def section(self):
        """ Returns a built in method. """

        return self._sections


class BotVars:
    """ Reads and sets the variables from the configuration file. """

    @staticmethod
    def read_config():
        """ Reads the variables from the configuration file. """
        ini_root = Path(__file__).parent.resolve()
        ini_file = ini_root / "vars.ini"
        config_sections = IniSection()
        config_sections.read(ini_file, "utf-8")
        parser = config_sections["VARS"].parser

        return parser

    def __init__(self):
        """ Sets up the environment variables once creating an instance."""
        parser = self.read_config()
        self.configs = dict(parser.section["BOT_CONFIGS"].items())
        self.users = dict(parser.section["BOT_USERS"].items())
        self.admin = parser.section["BOT_USERS"]["admin"]
