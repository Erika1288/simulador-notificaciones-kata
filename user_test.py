import unittest
from message import *
from user import *

class UserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('Erika')
    
    def test_constructor(self):
        self.assertEqual("Erika",self.user.name)
        self.assertTrue(self.user.id_user != '')
        self.assertTrue(len(self.user.inbox) == 0)
    
    def test_receive_message(self):
        message = Message("hello",1)
        self.user.receive_message(message)
        self.assertEqual(message,self.user.inbox[message.id_message])

    def test_read_message(self):
        message = Message("hello",1)
        self.user.receive_message(message)
        self.user.read_message(message)
        self.assertTrue(message.is_opened_by_user(self.user))
    
    


    































if __name__ == "__main__":
    unittest.main()