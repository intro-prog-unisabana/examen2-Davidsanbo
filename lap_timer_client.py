# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer

def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    archi= input("Nombre del archivo:")
    # TODO: Abrir el archivo y leer el numero de vueltas n
    with open(archi, "r") as miArchivo:
        n = int(miArchivo.readline())
    # TODO: Crear el cronometro usando lap_timer.init(n)
    timer = lap_timer.init(n)
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    with open(archi, "r") as miArchivo:
        n = int(miArchivo.readline())
        for _ in range(n):
            time = float(miArchivo.readline())
            lap_timer.add_lap(timer, time)
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    print(lap_timer.longest_decreasing_streak(timer))
    pass


if __name__ == "__main__":
    main()
