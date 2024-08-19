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
    """ Reads the vars from the configuration file. """
    ini_root = Path(__file__).parent.resolve()
    ini_file = ini_root / "vars.ini"

    def __init__(self):
        """ Sets up the environment variables once creating an instance."""
        config_sections = IniSection()
        config_sections.read(self.ini_file, "utf-8")
        parser = config_sections["VARS"].parser

        self.configs = dict(parser.section["BOT_CONFIGS"].items())
        self.users = dict(parser.section["BOT_USERS"].items())
        self.admin = parser.section["BOT_USERS"]["admin"]
