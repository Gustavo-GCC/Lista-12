import multiprocessing
import time
import random


index = multiprocessing.Value('i', 0)



def init(i, e):
    global index, entrada

    index = i
    entrada = e



def ordem(chegada):    
    match chegada:
        case 1:
            return "primeira"
        case 2:
            return "segunda"
        case 3:
            return "terceira"
        case 4:
            return "quarta"       
        


def entrando(p, c, s):
    tempo: int = 0

    print(f'{p} — que percorreu o corredor {c} em {s} segundos — foi a {ordem(index.value + 1)} pessoa a chegar à porta')
    
    tempo = random.randint(1, 2)
    time.sleep(tempo)

    print(f'{p} entrou ({tempo}s p/ concluir a ação)\n')

    index.value += 1    



def cruzando(pessoa, corredor):
    velocidade: int = 0
    distancia: int = 0
    posicao: int = 0
    segundos: int = 0

    velocidade = random.randint(4, 6) 
    distancia = 200    

    while (posicao < distancia):
        time.sleep(0.01)
        posicao += velocidade
        segundos += 1

    with entrada:
        entrando(pessoa, corredor, segundos)



def main():
    nome: str = ['Amélia', 'Balduíno', 'Celine', 'Dário']
    corredor: str = ['ALPHA', 'BETA', 'GAMMA', 'DELTA']

    corredores = list(zip(nome, corredor))


    with multiprocessing.Manager() as manager:
        entrada = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(index, entrada)) as pool:
            pool.starmap(cruzando, corredores)



if __name__ == '__main__':
    main()