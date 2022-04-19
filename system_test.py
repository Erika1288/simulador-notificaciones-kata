import unittest
from message import *
from user import *
from system import *

class SystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System(0)
    
    def test_constructor(self):
        self.assertTrue(len(self.system.users) == 0)
    
    def test_add_user(self):
        user = User("Erika")
        self.system.add_user(user)
        self.assertTrue(len(self.system.users) == 1)
    
    def test_getUsers(self):
        self.assertTrue(len(self.system.getUsers()) == 0)
        user = User("Erika")
        self.system.add_user(user)
        self.assertTrue(len(self.system.getUsers()) == 1)
        self.assertEqual(user,self.system.getUsers()[0])

    def test_publish_message(self):
        user = User("Erika")
        self.system.add_user(user)
        message = self.system.publish_message("hello")
        self.assertEqual(message,user.inbox[0])
        self.assertTrue(len(message.received_users_list)  == 1)

    
    def test_send_message_to_user(self):
        user = User("Erika")
        self.system.add_user(user)
        self.system.send_message_to_user("hello",user)
        self.assertTrue(len(user.inbox) == 1)



if __name__ == "__main__":
    unittest.main()