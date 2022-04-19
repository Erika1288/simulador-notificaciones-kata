import unittest
from message import *
from user import *

class MessageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.message = Message("hello",1)
    
    def test_constructor(self):
        self.assertEqual(1,self.message.id_message)
        self.assertEqual("hello",self.message.body)
        self.assertTrue(
            len(self.message.sended_user_list) == 0)
        self.assertTrue(
            len(self.message.received_users_list) == 0)
        self.assertTrue(
            len(self.message.opened_user_list) == 0)
        #falta comprobar la fecha
    
    def test_recived_by_user(self):
        user = User('Erika')
        self.message.recived_by_user(user)
        self.assertTrue(
            len(self.message.received_users_list) == 1)
    
    def test_opened_by_user(self):
        user = User('Erika')
        self.message.opened_by_user(user)
        self.assertTrue(
            len(self.message.opened_user_list) == 1)
    
    def test_is_opened_by_user(self):
        user = User('Erika')
        self.message.opened_by_user(user)
        self.assertTrue(self.message.is_opened_by_user(user))
        self.assertFalse(self.message.is_opened_by_user(User("Aaron")))
        

    




if __name__ == "__main__":
    unittest.main()