from app_scripts.main_entry import search
from app_scripts.state_functions import get_heuristic_by_positions, get_heuristic_zero, get_heuristic_by_distance

# Por meio da variável final_board é possível definir
# qualquer estado final que desejar, bastando pra isso
# definir a matriz final desejada

final_board = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]


# Variável que conterá a matriz de estado final desejado
init_board = []

# O estado inicial é lido a partir do arquivo board.pz
# devidamente armazenado na raiz do projeto

with open('board.pz') as fp:
    for line in fp:
        # todos os valores devem ser números inteiros
        numbers = [int(num) for num in line.split(',')]
        init_board.append(numbers)


solution, fringe, nodes_expanded = search(init_board=init_board, final_board=final_board, heuristic_function=get_heuristic_zero)

zero = open('heuristic_zero.txt', 'w')
zero.write(f'Expanded nodes: {nodes_expanded}\n')
zero.write(f'Fringe size: {fringe}\n')
zero.write(f'Actions: {solution}\n')
zero.close()

solution, fringe, nodes_expanded = search(init_board=init_board, final_board=final_board, heuristic_function=get_heuristic_by_positions)
position = open('heuristic_position.txt', 'w')
position.write(f'Expanded nodes: {nodes_expanded}\n')
position.write(f'Fringe size: {fringe}\n')
position.write(f'Actions: {solution}\n')
position.close()

solution, fringe, nodes_expanded = search(init_board=init_board, final_board=final_board, heuristic_function=get_heuristic_by_distance)
distance = open('heuristic_distance.txt', 'w')
distance.write(f'Expanded nodes: {nodes_expanded}\n')
distance.write(f'Fringe size: {fringe}\n')
distance.write(f'Actions: {solution}\n')
distance.close()



