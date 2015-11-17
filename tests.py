import unittest
 
class TestUM(unittest.TestCase):
      
    def setUp(self):
        pass
                  
    def test_numbers1(self):
        self.assertEqual(12, 12)
    
    def test_numbers2(self):
        self.assertEqual(12, 12)
    
    def test_numbers3(self):
        self.assertEqual(12, 12)
    
    def test_numbers4(self):
        self.assertEqual(12, 12)

if __name__ == '__main__':
    unittest.main()
