import unittest
import pinger
import shelve

class TestPingerUnit(unittest.TestCase): 

    def test_ping_should_return_true_for_online_user(self):
        self.assertTrue(pinger.ping('192.168.1.150'))

    def test_ping_should_return_false_for_offline_user(self):
        self.assertFalse(pinger.ping('192.168.1.199'))

    def test_ping_should_wake_a_mobile_device(self):
        self.assertTrue(pinger.ping('192.168.1.105'))
        
        

        

if __name__ == '__main__':
    unittest.main()
