import unittest

class TestWhosHome(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_smoke_test(self):
		self.assertEqual(2, 2)


if __name__ == '__main__':
	unittest.main()