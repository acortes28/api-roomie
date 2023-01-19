import peewee
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

database = peewee.MySQLDatabase("roomie",
                                host=config['DATABASE']['host'],
                                port=int(config['DATABASE']['port']),
                                user=config['DATABASE']['user'],
                                password=config['DATABASE']['pass']) 

