from bunch import Bunch

GAME_STATE = Bunch({'PLAYING': 0,
                    'DRAW': 1,
                    'CROSS_WON': 2,
                    'NOUGHT_WON': 3
                    })

current_state = GAME_STATE.PLAYING

SEED = Bunch({
    'EMPTY': 0,
    'CROSS': 1,
    'NOUGHT': 2
})

SEED_REPR = [' ', 'X', 'O']


def get_player_name(seed):
    return SEED_REPR[seed]
