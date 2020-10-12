import numpy as np
from .position_functions import position_can_move

# Verifica se o estado final do jogo foi alcançado
def is_final(board, final_board):
    for i, row in enumerate(board):
        for j, cel in enumerate(row):
            if final_board[i][j] != cel:
                return False
    return True

# Esta função sucessora produz um novo estado realizando
# a permuta entre a célula que contém o número 0 e uma célula vizinha
def successor_function(board, from_cel, to_cel):

    new_board = np.copy(board)

    # Esta variavel temporária foi utilizada apenas para facilitar
    # a leitura, mas poderia ser utilizado o método a,b = b,a
    temp_value = new_board[to_cel['i']][to_cel['j']]

    new_board[to_cel['i']][to_cel['j']] = new_board[from_cel['i']][from_cel['j']]
    new_board[from_cel['i']][from_cel['j']] = temp_value
    
    return new_board

# Retorna a heuristica considerando a posição de cada peça
def get_heuristic_by_positions(board, final_board):
    wrong_places = 0

    for i, row in enumerate(board):
        for j, cel in enumerate(row):
            if final_board[i][j] != cel:
                wrong_places += 1

    return wrong_places

# Retorna a heurística baseada na distância Manhatan
def get_heuristic_by_distance(board, final_board):

    for i, row in enumerate(board):
        for j, cel in enumerate(row):
            if cel == 0:
                manhatan_distance = i + j

    return manhatan_distance



# Retorna a mesma heurística igual a zero
# independentemente da posição das peças
def get_heuristic_zero(new_board, final_board):
    return 0