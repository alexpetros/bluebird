import unittest, pytest
from pandas import Timestamp
from bluebird.parsers import getChat

class FBChatTest(unittest.TestCase):

    TEST_FILE = './testing/fb_testdata/messages/convo1.html'

    TEST_USERS = ['Kurt Vonnegut', 'Leo Tolstoy', 'Virginia Woolf']
    TEST_CLIENT = 'Toni Morrison'
    TEST_COLUMNS = ['convo_id', 'message', 'sender', 'timestamp', 'wordcount']
    TEST_ROW = [None, 'Blsck', 'Leo Tolstoy', Timestamp('2011-03-08 04:13:00'), 5]
    TEST_LENGTH = 7
    
    def setUp(self):
        self.chat = getChat(open(self.TEST_FILE).read())

    def test_get_users(self):
        assert self.chat.users == self.TEST_USERS

    def test_get_client(self):
        assert self.chat.client == self.TEST_CLIENT

    def test_data_columns(self):
        data = self.chat.data
        assert list(data.columns.values) == self.TEST_COLUMNS

    def test_data_length(self):
        data = self.chat.data
        assert data['sender'].count() == self.TEST_LENGTH

    def test_data_message(self):
        data = self.chat.data
        assert list(data.loc[1].values) == self.TEST_ROW

    def test_non_fb_file(self):
        with pytest.raises(Exception):
            self.chat = getChat('NOT_A_FB_FILE')

