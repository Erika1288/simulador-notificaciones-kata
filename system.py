import random
import uuid
from user import *
from message import *

class System():
    
    def __init__(self,lost_average=10):
        """Create system with a list of users objects"""
        self.users = []
        self.lost_average = lost_average

    def add_user(self,user):
        """Add user to list"""
        self.users.append(user)
    
    def getUsers(self):
        """Get all users"""
        return self.users
    
    def publish_message(self,body)->Message: 
        """Create message with uuid and send to users addign a random lost"""
        message = Message(body,str(uuid.uuid1()))
        for user in self.users:
            random_lost = random.randint(0,100)
            if random_lost >= self.lost_average:
                user.receive_message(message)
                message.recived_by_user(user)
        return message
    
    def  send_message_to_user(self,body,user):
        """Send a message to a specific user"""
        for user1 in self.users:
            if user.name == user1.name:
                message = Message(body,str(uuid.uuid1()))
                user1.receive_message(message)
                message.recived_by_user(user1)

 
                



        




