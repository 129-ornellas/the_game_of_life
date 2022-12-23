import os
from time import sleep
from random import randint


def gera_grid(linha, coluna):
    return [[0] * coluna for l in range(linha)]


def grid_aleatorio(grid):
    for linha in range(1, len(grid) - 1):
        for coluna in range(1, len(grid[0]) - 1):
            grid[linha][coluna] = randint(0, 1)


def pega_vizinho(matriz, x, y):
    lado = 0 if matriz[x][y] == 0 else -1
    for _x in range(-1, 2):
        for _y in range(-1, 2):
            vizinho_x = x + _x
            vizinho_y = y + _y
            if (vizinho_x >= 0 and vizinho_y >= 0) and (vizinho_x < len(matriz) and vizinho_y < len(matriz[0])):
                lado += matriz[vizinho_x][vizinho_y]
    return lado


def print_grid(grid):
    for linha in grid:
        for coluna in linha:
            print("." if coluna == 0 else "#", end='')
        print()


def atualiza_matriz(matriz):
    nova_matriz = gera_grid(len(matriz), len(matriz[0]))
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            vizinho = pega_vizinho(matriz, linha, coluna)
            nova_matriz[linha][coluna] = int(
                (matriz[linha][coluna] == 0 and vizinho == 3)
                or (matriz[linha][coluna] == 1 and (not (vizinho < 2 or vizinho > 3)))
            )
    return nova_matriz


def main():
    grid = gera_grid(12, 12)
    grid_aleatorio(grid)
    try:
        while True:
            print_grid(grid)
            grid = atualiza_matriz(grid)
            sleep(0.4)
            os.system('clear')
    except KeyboardInterrupt:
        print('fechou!')


main()