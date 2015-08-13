import time

from main import GerarFizzBuzz

if __name__ == '__main__':
    lista = range(1, 10001)

    m0t1 = time.clock()
    GerarFizzBuzz(lista, 0)
    m0t2 = time.clock()

    m1t1 = time.clock()
    GerarFizzBuzz(lista, 1)
    m1t2 = time.clock()

    m2t1 = time.clock()
    GerarFizzBuzz(lista, 2)
    m2t2 = time.clock()

    deltam0 = m0t2 - m0t1
    deltam1 = m1t2 - m1t1
    deltam2 = m2t2 - m1t1

    print("Tempo do Metodo 0:", deltam0, "segundos")
    print("Tempo do Metodo 1:", deltam1, "segundos")
    print("Tempo do Metodo 2:", deltam2, "segundos")
