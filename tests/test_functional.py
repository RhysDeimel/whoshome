import unittest
import pinger
import shelve
import datetime
import time

class TestPingerFunctional(unittest.TestCase):

    # User runs pinger and it updates known the connection status of
    # known devices, and their timestamp/ last seen time.
    def test_known_active_ip_is_changed_to_true(self):
        with shelve.open('userdb', writeback=True) as db:
            db['users']['rhys']['ip']['192.168.1.150']['online'] = False # this is the dev pc -> should be on
        pinger.runner()
        with shelve.open('userdb', writeback=True) as db: 
            self.assertTrue(db['users']['rhys']['ip']['192.168.1.150']['online'])

    def test_timestamp_is_updated_on_active_ip(self):
        temp_time = datetime.datetime.now()
        with shelve.open('userdb', writeback=True) as db:
            db['users']['rhys']['ip']['192.168.1.150']['seen'] = temp_time
        time.sleep(3)
        pinger.runner()
        with shelve.open('userdb', writeback=True) as db:
            self.assertNotEqual(db['users']['rhys']['ip']['192.168.1.150']['seen'], temp_time)

    def test_last_seen_is_calculated_for_inactive(self):
        timestamp = datetime.datetime.strptime('2017-02-26 01:22:09.489923', '%Y-%m-%d %H:%M:%S.%f')
        with shelve.open('userdb', writeback=True) as db:
            db['users']['rhys']['ip']['192.168.1.111']['seen'] = timestamp
        time.sleep(3)
        pinger.runner()
        with shelve.open('userdb', writeback=True) as db:
            self.assertNotEqual(db['users']['rhys']['ip']['192.168.1.111']['seen'], timestamp)
            print(db['users']['rhys']['ip']['192.168.1.150']['seen'])
    # with everything updated, a jinja template will be populated

    # the outputted html file will then be moved to the appropriate
    # directory

    # The webpage should be served, and visible to the world

if __name__ == '__main__':
    unittest.main()
