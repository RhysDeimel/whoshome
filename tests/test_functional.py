import unittest
import pinger
import shelve

class TestPingerFunctional(unittest.TestCase):

    def setUp(self):
        self.db = shelve.open('userdb')

    def tearDown(self):
        self.db.close()

    # User runs pinger and it loops through a list (userdb) of users
    # and determines if they are online or offline
    # If they are, is sets status to true and updates timestamp
    def test_should_confirm_if_user_online(self):
        self.assertEqual(self.db['users']['rhys']['device']['desktop']['online'], True) # This is dev PC and should be on

    def test_timestamp_should_be_updated(self):
        pass

    # If they aren't, sets status to false and calculates last seen
    def test_should_confirm_if_user_offline(self):
        self.assertEqual(self.db['users']['rhys']['device']['laptop']['online'], False) # This is work PC and should be off

    def test_should_calculate_last_seen(self):
        pass

    # with everything updated, a jinja template will be populated

    # the outputted html file will then be moved to the appropriate
    # directory

    # The webpage should be served, and visible to the world

if __name__ == '__main__':
    unittest.main()
