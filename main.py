import agent
import othello
import game
import sys

def create_player(arg):
    if arg == 'human':
        return agent.HumanPlayer()
    elif arg == 'random':
        return agent.RandomAgent()
    elif arg == 'minimax':
        depth = input("Depth for MiniMax: ")
        return agent.MinimaxAgent(int(depth))
    elif arg == 'alphabeta':
        depth = input("Depth for AB_MiniMax: ")
        return agent.AlphaBeta(int(depth))
    else:
        agent.RandomAgent()

def get_arg(index, default=None):
    '''Returns the command-line argument, or the default if not provided'''
    return sys.argv[index] if len(sys.argv) > index else default

if __name__ == '__main__':

    initial_state = othello.State()

    if len(sys.argv) > 1:
        agent1 = sys.argv[0]
        agent2 = sys.argv[1]
        


    player1 = create_player(get_arg(1))
    player2 = create_player(get_arg(2))

    # player1 = agent.HumanPlayer()
    # player2 = agent.RandomAgent()

    game = game.Game(initial_state, player1, player2)

    game.play()

    