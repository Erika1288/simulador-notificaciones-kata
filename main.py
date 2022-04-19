import time
from user import *
from message import *
from system import *
import logging
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger = logging.getLogger()

user1 = User('erika')
user2 = User('aaron')
sistema = System()
sistema.add_user(user1)
sistema.add_user(user2)
sistema.send_message_to_user("hola como estas",user1)

for user in range(1000):
    sistema.add_user(User('Vinka'))
time.sleep(3)
mensaje1 = sistema.publish_message('lo que sea')
time.sleep(3)
mensaje2 = sistema.publish_message('hola que tal')
user1.read_message(mensaje1)
user1.view_inbox()
mensaje1.statistics()

sistema.send_message_to_user('hola que tal',user1)
sistema.send_message_to_user('hola que tal',user1)
sistema.send_message_to_user('hola que tal',user1)



user1.view_inbox()
mensaje1.statistics()
