##Grant Reynard
import sys
import math
import random
import game
import time


class HumanPlayer(game.Player):
    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]


#subcalss of player
class RandomAgent(game.Player):
    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()
        # print(moves[1])
        if len(moves) == 0:
            return None
        else:
            r = random.randint(0, len(moves) - 1)
            return moves[r]


class MinimaxAgent(game.Player):
    def __init__(self, depth):
        self.depth = depth
        self.average = 0
        self.move_count = 0
        super().__init__()

    def choose_move(self, state):
        moves = state.generateMoves()
        if moves:
            t1 = time.perf_counter()
            mm_move = self.minimax(state, self.depth, state.nextPlayerToMove)
            t2 = time.perf_counter()
            self.average = (self.average * self.move_count +
                            (t2 - t1)) / (self.move_count + 1)
            self.move_count += 1
            print("Running average for MiniMax of Depth", self.depth, ":",
                  self.average)
            return moves[mm_move]
        else:
            return None

    def minimax(self, state, depth, player_bool):
        if depth == 0:
            return state.score()
        else:
            moves = state.generateMoves(player_bool)
            if len(moves) == 0:
                return state.score()
            if player_bool:
                max_ = -(sys.maxsize)
                max_move = 0
                for i in range(0, len(moves)):
                    temp = state.applyMoveCloning(moves[i])
                    score = self.minimax(temp, depth - 1, not player_bool)
                    if max_ < score:
                        max_ = score
                        max_move = i
                # print("max",max_move)
                return max_move
            else:
                min_move = 0
                min_ = sys.maxsize
                for i in range(0, len(moves)):
                    temp = state.applyMoveCloning(moves[i])
                    score = self.minimax(temp, depth - 1, not player_bool)
                    if min_ > score:
                        min_ = score
                        min_move = i
                return min_move


class AlphaBeta(game.Player):
    def __init__(self, depth):
        self.depth = depth
        self.average = 0
        self.move_count = 0
        super().__init__()

    def choose_move(self, state):
        moves = state.generateMoves()
        if moves:
            t1 = time.perf_counter()
            ab_move = self.ABminimax(state, self.depth, state.nextPlayerToMove,
                                     -(sys.maxsize), sys.maxsize)
            t2 = time.perf_counter()
            self.average = (self.average * self.move_count +
                            (t2 - t1)) / (self.move_count + 1)
            self.move_count += 1
            print("Running average for AlphaBeta of Depth", self.depth, ":",
                  self.average)
            return moves[ab_move]
        else:
            return None

    def ABminimax(self, state, depth, player_bool, a, b):
        if depth == 0:
            return state.score()
        else:
            moves = state.generateMoves(player_bool)
            if len(moves) == 0:
                return state.score()
            if player_bool:
                max_ = -(sys.maxsize)
                max_move = 0
                for i in range(0, len(moves)):
                    temp = state.applyMoveCloning(moves[i])
                    score = self.ABminimax(temp, depth - 1, not player_bool, a,
                                           b)
                    if max_ < score:
                        max_ = score
                        max_move = i
                    a = max(a, max_)
                    if b <= a:
                        break
                # print("max",max_move)
                return max_move
            else:
                min_move = 0
                min_ = sys.maxsize
                for i in range(0, len(moves)):
                    temp = state.applyMoveCloning(moves[i])
                    score = self.ABminimax(temp, depth - 1, not player_bool, a,
                                           b)
                    if min_ > score:
                        min_ = score
                        min_move = i
                    b = min(b, min_)
                    if b <= a:
                        break
                return min_move
