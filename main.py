import unittest

def GerarFizzBuzz(listaDeNumeros, metodo=0):
    # novaLista = list(range(0, len(listaDeNumeros)))
    novaLista = []
    if metodo == 0:
        # for i in range(0, len(listaDeNumeros)):
            # novaLista[i] = fizzbuzz(listaDeNumeros[i])
        for i in listaDeNumeros:
            novaLista.append(fizzbuzz(i))
    elif metodo == 1:
        novaLista = [fizzbuzz(x) for x in listaDeNumeros]
    elif metodo == 2:
        novaLista = list(map(fizzbuzz, listaDeNumeros))

    return novaLista

def fizzbuzz(valor):
    retorno = ""

    if valor%3 == 0:
        retorno += 'Fizz'
    if valor%5 == 0:
        retorno += 'Buzz'

    if retorno == "":
        retorno = str(valor)

    return retorno

class TestAdd(unittest.TestCase):
    ListaDeNumeros = list(range(1,101))

    def testarTamanhoLista(self):
        self.assertEqual(len(self.ListaDeNumeros), 100)

    def testarTamanhoListaNoMetodo(self):
        self.assertEqual(len(GerarFizzBuzz(self.ListaDeNumeros)), 100 )
    def testarFizzBuzzValorUm(self):
        self.assertEqual(fizzbuzz(1), "1")
    def testarFizzBuzzValorDois(self):
        self.assertEqual(fizzbuzz(2), "2")
    def testarFizzBuzzValorQuatro(self):
        self.assertEqual(fizzbuzz(4), "4")
    def testarFizzBuzzValorTres(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    def testarFizzBuzzValorSeis(self):
        self.assertEqual(fizzbuzz(6), "Fizz")
    def testarFizzBuzzValorNove(self):
        self.assertEqual(fizzbuzz(9), "Fizz")
    def testarFizzBuzzValorCinco(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    def testarFizzBuzzValorSete(self):
        self.assertEqual(fizzbuzz(7), "7")
    def testarFizzBuzzValorDez(self):
        self.assertEqual(fizzbuzz(10), "Buzz")
    def testarFizzBuzzValorQuize(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    def testarFizzBuzzValorQuize(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def testarListaFizzBuzzComUmElemento(self):
        lista = GerarFizzBuzz([1])

        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0], "1")

    def testarListaFizzBuzzComDoisElemento(self):
        lista = GerarFizzBuzz([3, 5])

        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[0], "Fizz")
        self.assertEqual(lista[1], "Buzz")

    def testarListaFizzBuzzComVariosElemento(self):
        lista = GerarFizzBuzz([1, 3, 5, 15, 7])

        self.assertEqual(len(lista), 5)
        self.assertEqual(lista[0], "1")
        self.assertEqual(lista[1], "Fizz")
        self.assertEqual(lista[2], "Buzz")
        self.assertEqual(lista[3], "FizzBuzz")
        self.assertEqual(lista[4], "7")

if __name__ == '__main__':
    unittest.main()
