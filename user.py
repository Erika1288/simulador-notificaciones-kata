import uuid
import collections
import textwrap

from message import *

class User():

    def __init__(self,name):
        """Create user name, id and an empty inbox"""
        self.inbox = dict()
        self.name = name 
        self.id_user = str(uuid.uuid1())

    def receive_message(self,message):
        """Index the message by id in inbox"""   
        self.inbox[message.id_message] = message 

    def read_message(self,message_p):
        """Read the message by user"""
        for message in self.inbox.items():
            if message[0] == message_p.id_message:
                print(f"\nreaded message: {message[1].body}")
                message_p.opened_by_user(self)
                  
    def view_inbox(self):
        """View inbox ordered by date"""
        ordered_inbox = collections.OrderedDict(sorted(self.inbox.items(), key=lambda message: message[1].date) )
    
        for message in ordered_inbox.items():
            if message[1].is_opened_by_user(self) == True: 
                readed_message = textwrap.dedent(f"""
                READED MESSAGGES: 
                DATE: {message[1].humanDate} 
                ID MESSAGE: {message[0]}
                STATUS: readed""") 
                print(readed_message)
            else:
                unread_message = textwrap.dedent(f"""
                UNREAD MESSAGGES: 
                DATE: {message[1].humanDate} 
                ID MESSAGE: {message[0]}
                STATUS: unread""") 
                print(unread_message)
                