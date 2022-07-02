# Crear prueba unitaria básica 
import unittest 


class TestBasico(unittest.TestCase):
    def test_es_menor_que(self):
        self.assertTrue(2<3);

if __name__ == "__main__":
    unittest.main()