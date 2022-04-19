import datetime
import logging
import textwrap
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger = logging.getLogger()
from user import * 

class Message():

    def __init__(self,body,message_id):
        """Create message constructor"""
        self.date = datetime.datetime.now()
        self.humanDate = self.date.strftime("%A %d %B %Y - %H:%M:%S")
        self.sended_user_list = []
        self.received_users_list = []
        self.opened_user_list = []
        self.body = body
        self.id_message = message_id
               
    def recived_by_user(self,user):
        """Add to a list of users recived message"""
        self.received_users_list.append(user)

    def opened_by_user(self,user):
        """Add to a list of users opened a message"""
        self.opened_user_list.append(user)
    
    def is_opened_by_user(self,user_p):
        """Verify if a user has opened a message"""
        for user in self.opened_user_list:
            if user.id_user == user_p.id_user:
                logging.info(f"User : {user.name} has opened a message\n")
                return True
        return False
    
    def statistics(self):
        """Show statistics of messages"""
        statistics = textwrap.dedent(f"""
            The message: {self.id_message}
            Has send by: {len(self.sended_user_list)} users 
            Date: {self.humanDate}
            Received by: {len(self.received_users_list)} users Opened by: {len(self.opened_user_list)} users
            """)
        print(statistics)
    