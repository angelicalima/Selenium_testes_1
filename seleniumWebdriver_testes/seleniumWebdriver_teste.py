from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 

class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit) # ou usar metodo teardown

    def test_pesquisa_titulo(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def test_pesquisa(self):
        self.browser.get('http://www.google.com')
        textBoxPesquisa = self.browser.find_element_by_name("q")
        textBoxPesquisa.send_keys("angelica")
        textBoxPesquisa.submit()
        try:
            # Verificar se a pagina carregou (10 segundos)
            WebDriverWait(self.browser, 10).until(EC.title_contains("angelica - Pesquisa Google"))
        finally:
            self.assertIn('angelica - Pesquisa Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)