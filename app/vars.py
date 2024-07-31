import configparser


class IniSection(configparser.ConfigParser):
    @property
    def section(self):
        return self._sections


class BotVars:
    def __init__(self):
        config_sections = IniSection()
        config_sections.read("vars.ini", "utf-8")
        parser = config_sections["VARS"].parser
        self.bot_configs = {
            par_name.upper(): par_value
            for par_name, par_value
            in parser.section["BOT_CONFIGS"].items()
        }
        self.bot_users = {
            user_name.upper(): user_id
            for user_name, user_id
            in parser.section["BOT_USERS"].items()}
