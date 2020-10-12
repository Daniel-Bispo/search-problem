import matplotlib.pyplot as plt
from heapq import heappush, heappop

from .state_functions import is_final, successor_function
from .position_functions import get_next_action

# Função principal que realiza a busca A*
def search(init_board=[], final_board=[], heuristic_function=None):

    fringe = []

    # Inicializa a fila com o nodes que serão expandidos
    heappush(fringe, (0, [], init_board))

    # Contador para posterior verificação do total de nodes expandidos
    nodes_expanded_counter = 0

    # As expansões ocorrerão Enquanto houver nodes fringe
    while len(fringe):
        
        # Retira o fringe com a maior prioridade, ou seja,
        # com o custo total mais baixo
        node = heappop(fringe)
       
        _, actions, board = node

        nodes_expanded_counter += 1

        # Retorna o resultado ao chegar a solução desejada
        if is_final(board, final_board):   
            # Captura apenas o nome dos movimento realizados para
            # simplificar a leitura da solução         
            all_actions = [action[0] for action in actions]
            return all_actions, len(fringe), nodes_expanded_counter
        else:
            # Se a solução ainda não ter sido encontrada,
            # avalia as possíveis ações a partir do node atual
            next_actions = get_next_action(board)

            for action in next_actions:
                # Coleta as células da matriz que terão
                # os seus valores permutados
                from_cel = action[1]['from']
                to_cel = action[1]['to']

                # Por meio da função sucessora (sucessor_function) é possível
                # avaliar a heurística para o próximo estado (new_board)
                new_board = successor_function(board, from_cel, to_cel)          

                heurisct_cost = heuristic_function(new_board, final_board)
                cost_cost = len(actions) + 1
                
                # Após calcular a heurística (heuristic_cost) e o
                # custo (cost_cost) da ação é possível definir
                # a prioridade (node_priority) de expansão do node por meio do
                # custo acumulado
                node_priority = cost_cost + heurisct_cost

                actions_list = actions + [ action ]

                # O node entra no fringe de acordo com a prioridade
                heappush(fringe, (node_priority, actions_list, new_board))


    return None, len(fringe), nodes_expanded_counter
