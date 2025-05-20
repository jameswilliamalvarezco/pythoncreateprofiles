import unittest

class TestPasses(unittest.TestCase):    
    def PipelineTest(self):
        self.assertTrue(True)
        
    def test_fail(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()