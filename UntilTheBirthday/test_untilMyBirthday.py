import unittest
import delta
import datetime

class TestUntilMyBirthday(unittest.TestCase):
    def test_birthday(self):
        today = datetime.date.today()
        result = delta.deltaCounting(today.day, today.month)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
