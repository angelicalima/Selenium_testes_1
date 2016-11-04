from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 


#para pesquisa em xml utilizar xpath
#http://www.w3schools.com/xml/xpath_syntax.asp

class SubmarinoTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_preco_produto(self):
        self.browser.get('http://www.submarino.com')
        textBoxPesquisa = self.browser.find_element_by_id("h_search-input")
        textBoxPesquisa.send_keys("dell 2 em 1 i7")
        textBoxPesquisa.submit()

        #pesquisa em Xpath:
        #"//span[@property ='price' and @class='value']"
        # para pesquisar no console do mozila utilizar $# antes da consulta. ex:$x("//span[@property ='price' and @class='value']")
        #@ para propriedades da tag
        #// para procrurar todas as tags "span"
        try:
            # Verificar se a pagina carregou (40 segundos)
            WebDriverWait(self.browser, 40).until(EC.title_contains("dell 2 em 1 i7"))
        finally:
            self.assertIn('dell 2 em 1 i7', self.browser.title)
            arrayPriceConsulta = self.browser.find_elements_by_xpath("//span[@property ='price' and @class='value']")
            for i in arrayPriceConsulta:
                print(i.text) # text eh um atributo dentro de cada elemento do array da consulta
                self.assertGreater(i.text,0)
                
if __name__ == '__main__':
    unittest.main(verbosity=2)