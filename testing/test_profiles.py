import unittest, pytest
from bluebird.profiles import getProfile

class FBProfileTest(unittest.TestCase):

    TEST_FOLDER = './testing/fb_testdata' 

    def setUp(self):
        self.profile = getProfile(TEST_FOLDER)