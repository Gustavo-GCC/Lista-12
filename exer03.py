import multiprocessing
import time
import random


index = multiprocessing.Value('i', 1)
pista = multiprocessing.Value('i', 0)


def init(p, i, c):
    global pista, index, chegada

    pista = p
    index = i
    chegada = c



def podio(n, s, t):
    print(f'SAPO: {n}\n\tPOSIÇÃO: {index.value}º\n\tTAMANHO DO SALTO: {s}cm\n\tTEMPO: {t}s\n')

    index.value += 1



def corrida(nome):
    global chegada
    salto: int = 0
    posicao: int = 0
    tempo: int = 0

    salto = random.randint(1, 5)

    while (posicao < pista):
        time.sleep(0.01)
        posicao += salto
        tempo += 1

    with chegada:
        podio(nome, salto, tempo)



def main():
    global pista

    sapo = [
        'Gamabunta',
        'Greninja',
        'Kermit',
        'Pepe',
        'Rash'
    ]    

    pista = random.randint(10, 50)
    print(f'\n\t\tTAMANHO DA PISTA DE CORRIDA: {pista}cm\n')


    with multiprocessing.Manager() as manager:
        chegada = manager.Semaphore(1)

        with multiprocessing.Pool(processes=5, initializer=init, initargs=(pista, index, chegada)) as pool:
            pool.map(corrida, sapo)


if __name__ == '__main__':
    main()