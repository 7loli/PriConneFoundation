import random

ALIVE_LIST = []
WEED_LIST = []
NUMBER = 100
INIT_SCORE = 5000
GAMER = {
    'No.': 0,
    'Score': INIT_SCORE
}


def init():
    for i in range(1, NUMBER + 1):
        gamer = GAMER.copy()
        gamer['No.'] = i
        ALIVE_LIST.append(gamer)


def get_list(l=ALIVE_LIST):
    for gamer in l:
        print(gamer)


def sort_group(l=ALIVE_LIST):
    if len(l) >= 4:
        group = ALIVE_LIST[:2] + ALIVE_LIST[:2]


def group_match(group:list):
    pass


def score_calculate(gamer:dict):
    pass


if __name__ == '__main__':
    init()
    get_list()

