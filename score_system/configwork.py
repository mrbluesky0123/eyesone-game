import yaml
import os
import configwork

def get_config():
    config_file = open('appconfig.yaml', 'r')
    config = yaml.load(config_file, Loader=yaml.BaseLoader)
    config_file.close()
    return config