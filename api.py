from configparser import ConfigParser

config = ConfigParser()
configpath = './'
config.read(f'{configpath}config.ini')

print(config["SUNSKY"]["key"])
print(config["SUNSKY"]["secret"])