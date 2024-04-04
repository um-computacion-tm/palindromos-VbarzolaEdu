import unittest

def es_palindromo(string):
   
   string = string.lower().replace(" ", "")

   if string == string [::-1]:
        return True
   else:
        return False      


class TestPalindromo(unittest.TestCase):
    def test_1(self):
        result = es_palindromo("neuquen")
        self.assertEqual(result, True)
    
    def test_2(self):
        result = es_palindromo("aca")
        self.assertEqual(result, True)

    
    def test_3(self):
        result = es_palindromo("stermo")
        self.assertEqual(result, False)

    def test_4(self):
        result = es_palindromo("anita lava la tina")
        self.assertEqual(result,True)

    def test_5(self):
        result = es_palindromo("francisco#")
        self.assertEqual(result, False)
        
            

    
unittest.main()