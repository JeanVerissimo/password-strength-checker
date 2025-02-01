import unittest
import unittest.mock
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_empty_password(self):
        self.assertIsNone(main.calc_entropy(''))
    
    def test_invalid_password(self):
        self.assertIsNone(main.calc_entropy('a b c'))

    def test_api(self):
        response = main.request_api_data('ABCDE')
        self.assertEqual(response.status_code, 200)
    
    def test_failed_api(self):
        self.assertIsNone(main.request_api_data(''))

    

if __name__ == '__main__':
    unittest.main()