import multiprocessing


sentido = ['Leste', 'Norte', 'Oeste', 'Sul']
index = multiprocessing.Value('i', 0)



def init(i, s):
    global index, semaforo
    index = i
    semaforo = s



def trafego(id):   
    with semaforo:
        print(f'O {id + 1}º carro está atravessando para o {sentido[index.value]}')
        print('Travessia concluída\n')
        index.value += 1



def main():
    veiculo: int = [0]*4
    semaforo = None

    for j in range(4):
        veiculo[j] = j

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(index, semaforo)) as pool:
            pool.map(trafego, veiculo)



if __name__ == '__main__':
    main()