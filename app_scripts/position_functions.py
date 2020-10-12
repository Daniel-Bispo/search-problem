# Retorna as possíveis ações de acordo com a posição atual
def position_can_move(i, j, board, cel):
    movements = {}

    # Verifica se pode mover para o Norte
    if i > 0:
        north = {
            'to': {
                'i': i - 1,
                'j': j
            },
            'from': {
                'i': i,
                'j': j
            }

        }
        movements['north'] = north

    # Verifica se pode mover para o Sul
    if i < 2:
        south = {
            'to': {
                'i': i + 1,
                'j': j
            },
            'from': {
                'i': i,
                'j': j
            }
        }
        movements['south'] = south

    # Verifica se pode mover para o Oeste
    if j > 0:
        west = {
            'to': {
                'i': i,
                'j': j - 1
            },
            'from': {
                'i': i,
                'j': j
            }
        }
        movements['west'] = west

    # Verifica se pode mover para o Leste
    if j < 2:
        east = {
            'to': {
                'i': i,
                'j': j + 1
            },
            'from': {
                'i': i,
                'j': j
            }
        }
        movements['east'] = east

    return movements

# Verifica todas as possibilidades a partir da posição do zero
def get_next_action(board):
    next_actions = []

    for i, row in enumerate(board):
        for j, cel in enumerate(row):
            if cel == 0:
                next_actions = [action for action in position_can_move(i, j, board, cel).items()]

    return next_actions
    