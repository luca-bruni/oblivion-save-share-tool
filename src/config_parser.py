from configparser import ConfigParser

class ConfigManager:
    def __init__(self):
        self.config_parser = ConfigParser()

    def get_config(self):
        try:
            with open('../config.ini') as f:
                self.config_parser.read_file(f)
        except IOError:
            print("Error reading config.ini: File not found")
            return None

        try:
            oblivion_directory = self.config_parser.get('oblivion properties', 'oblivion_directory')
            character_name = self.config_parser.get('oblivion properties', 'character_name')
        except:
            print("Error reading config.ini: Incorrect file format")
            return None

        return ConfigObject(oblivion_directory, character_name)

class ConfigObject:
    def __init__(self, oblivion_directory, character_name):
        self.oblivion_directory = oblivion_directory
        self.character_name = character_name