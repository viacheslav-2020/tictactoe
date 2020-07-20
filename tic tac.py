user1_name = input('User1, what is your name?')
print('')
print('Welcome {}'.format(user1_name))
print('')
user2_name = input('User2, what is your name?')
print('Welcome {}'.format(user2_name))
print('')

# Доска
board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

board_image = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

print('')
print(board_image[0])
print(board_image[1])
print(board_image[2])
print('')

# победные ходы
winning_moves=[
    [1,4,7],
    [1,2,3],
    [7,8,9],
    [3,6,9],
    [3,5,7],
    [1,5,9]
]

user1_moves=[]
user2_moves=[]

def smbd_won(hodi):
    for i in winning_moves:
#        print(i)
        if (i[0] in hodi) and (i[1] in hodi) and (i[2] in hodi):
            return True

def board_show():
    for i in user1_moves:
        if i == 1:
            board_image[0][0] = 'x'
        elif i == 2:
            board_image[0][1] = 'x'
        elif i == 3:
            board_image[0][2] = 'x'
        elif i == 4:
            board_image[1][0] = 'x'
        elif i == 5:
            board_image[1][1] = 'x'
        elif i == 6:
            board_image[1][2] = 'x'
        elif i == 7:
            board_image[2][0] = 'x'
        elif i == 8:
            board_image[2][1] = 'x'
        elif i == 9:
            board_image[2][2] = 'x'

    for i in user2_moves:
        if i == 1:
            board_image[0][0] = 'o'
        elif i == 2:
            board_image[0][1] = 'o'
        elif i == 3:
            board_image[0][2] = 'o'
        elif i == 4:
            board_image[1][0] = 'o'
        elif i == 5:
            board_image[1][1] = 'o'
        elif i == 6:
            board_image[1][2] = 'o'
        elif i == 7:
            board_image[2][0] = 'o'
        elif i == 8:
            board_image[2][1] = 'o'
        elif i == 9:
            board_image[2][2] = 'o'

    print(board_image[0])
    print(board_image[1])
    print(board_image[2])

def check_move(move):
    if move in list(set(user1_moves+user2_moves)):
        print('this move is already done. chose another')
        return False
    else:
        print('move is: {}'.format(move))
        return True

user_input = False

while (len(user1_moves) + len(user2_moves)) <= 8:
    while user_input == False:
        u1 = input('{}, your next move ?'.format(user1_name))
        u1=int(u1)
#        print('u1 = ', u1, 'type ', type(u1))
        user_input = check_move(u1)
    user1_moves.append(u1)
#    print('user1_moves', user1_moves)
    board_show()
    if smbd_won(user1_moves):
        print('{} is the winner! Congrats!'.format(user1_name))
        break
#    print('len user1_moves = {}'.format(len(user1_moves)))
    user_input = False

    if (len(user1_moves) + len(user2_moves)) >= 9:
        print('it looks like a draw')
        print('Game over')
        break

    while user_input == False:
        u2 = input('{}, your next move ?'.format(user2_name))
        u2=int(u2)
 #       print('u2 = ',u2,'type ', type(u2))
        user_input = check_move(u2)
    user2_moves.append(u2)
    board_show()
    if smbd_won(user2_moves):
        print('{} is the winner! Congrats!'.format(user2_name))
        break
#    print('len user2_moves = {}'.format(len(user2_moves)))
    user_input = False
#    print('len total = ', len(user1_moves)+len(user2_moves))


if (smbd_won(user1_moves) == False) and (smbd_won(user2_moves) == False):
    print('it looks like draw')