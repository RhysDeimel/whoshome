import unittest
import pinger
import shelve

class TestPingerUnit(unittest.TestCase):

    def test_get_device_ip_list_returns_list_of_ip_strings(self):
        ip_list = ['192.168.1.150', '192.168.1.111', '192.168.1.105']
        self.assertEqual(pinger.get_device_ip_list().sort(), ip_list.sort()) 

    def test_ping_should_return_true_for_online_user(self):
        self.assertTrue(pinger.ping('192.168.1.150'))

    def test_ping_should_return_false_for_offline_user(self):
        self.assertFalse(pinger.ping('192.168.1.199'))

    def test_ping_should_wake_a_mobile_device(self):
        self.assertTrue(pinger.ping('192.168.1.105'))

    def test_update_device_status_false_to_true(self):
        # check to see if returns true
        self.assertTrue(pinger.update_device_status('rhys', 'laptop'))

    def test_update_device_status_true_to_false(self):
        # check to see if returns false
        self.assertFalse(pinger.update_device_status('rhys', 'desktop'))
        
        

        

if __name__ == '__main__':
    unittest.main()
