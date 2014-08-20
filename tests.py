import unittest
import my_package


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_package.add(10), 20)

if __name__ == '__main__':
    unittest.main()
