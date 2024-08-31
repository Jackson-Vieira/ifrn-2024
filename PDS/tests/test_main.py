import unittest
from main import Pessoa

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.pessoa = Pessoa('Fulano', '123.456.789-00', 20)

    def test_str(self):
        self.assertEqual(str(self.pessoa), 'Nome: Fulano, Idade: 20, CPF: 123.456.789-00')

    def test_get_cpf(self):
        self.assertEqual(self.pessoa.get_cpf(), '123.456.789-00')

    def test_set_cpf(self):
        self.pessoa.set_cpf('987.654.321-00')
        self.assertEqual(self.pessoa.get_cpf(), '987.654.321-00')

    def test_get_idade(self):
        self.assertEqual(self.pessoa.get_idade(), 20)

    def test_set_idade(self):
        self.pessoa.set_idade(30)
        self.assertEqual(self.pessoa.get_idade(), 30)

if __name__ == "__main__":
    unittest.main()
