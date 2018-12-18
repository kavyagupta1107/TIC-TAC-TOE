def print_states(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])


def win_status(state, player):
    if state[0] == player and state[1] == player and state[2] == player:
        return 'win'
    if state[3] == player and state[4] == player and state[5] == player:
        return 'win'
    if state[6] == player and state[7] == player and state[8] == player:
        return 'win'
    if state[0] == player and state[3] == player and state[6] == player:
        return 'win'
    if state[1] == player and state[4] == player and state[7] == player:
        return 'win'
    if state[2] == player and state[5] == player and state[8] == player:
        return 'win'
    if state[0] == player and state[4] == player and state[8] == player:
        return 'win'
    if state[2] == player and state[4] == player and state[6] == player:
        return 'win'
    for place in range(0, 9):
        if state[place] == 0:
            return

    return 'tie'


player = 1
position = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print_states(board)
while True:
    print("player", player)
    while True:
        turn = eval(input("make a move"))
        valid_moves = []
        for position in range(0, 9):
            if board[position] == 0:
                valid_moves.append(position)
        print(valid_moves)
        if turn in valid_moves:
            break
        print("Illegal move")

    board[turn] = player
    print_states(board)
    status = win_status(board, player)
    if status == 'win':
        print("player", player, "wins")
        break
    if status == 'lose':
        print("player", player, "loses")
        break
    if status == 'tie':
        print("tie")
        break
    if player == 1:
        player = 2
    else:
        player = 1

print("game is so over")



