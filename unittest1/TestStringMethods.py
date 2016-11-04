import unittest 
import binascii

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('angelica'.upper(), "ANGELICA")

    def test_true(self):
        self.assertTrue("ANDRE".isupper())

    def test_false(self):
        self.assertFalse("ANDRE".islower())

    def test_invalid_arg(self):
        #verifica excecoes
        with self.assertRaises(TypeError):
            binascii.hexlify('a')

if __name__== '__main__':
    unittest.main()
    input()

