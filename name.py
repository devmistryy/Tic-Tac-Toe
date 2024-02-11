class player():
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
    
    def __repr__(self):
        return self.name + '(' + self.letter + ')'

    def get_name(self):
        return self.name
    
    def get_letter(self):
        return self.letter

def check_tie():
    temp = True
    for val in ticdict.values():
        if val == ' ':
            temp = False
    return temp

def check_win(input_player):
    k = input_player.get_letter()
    if ((ticdict[11] == k and ticdict[12] == k and ticdict[13] == k) 
        or (ticdict[21] == k and ticdict[22] == k and ticdict[23] == k) 
        or (ticdict[31] == k and ticdict[32] == k and ticdict[33] == k) 
        or (ticdict[11] == k and ticdict[21] == k and ticdict[31] == k) 
        or (ticdict[12] == k and ticdict[22] == k and ticdict[32] == k) 
        or (ticdict[13] == k and ticdict[23] == k and ticdict[33] == k) 
        or (ticdict[11] == k and ticdict[22] == k and ticdict[33] == k) 
        or (ticdict[13] == k and ticdict[22] == k and ticdict[31] == k)):
        return True
    return False

def print_table():
    print(' ' + str(ticdict[11]) +  '| ' + str(ticdict[12]) + ' | ' + str(ticdict[13]))
    print('--|---|--')
    print(' ' + ticdict[21] + '| ' + ticdict[22] + ' | ' + ticdict[23])
    print('--|---|--')
    print(' ' + ticdict[31] + '| ' + ticdict[32] + ' | ' + ticdict[33])
    print('Current Player: ' + str(current_player))


player1 = player('Player 1', 'X')
player2 = player('Player 2', 'O')
current_player = player1

ticdict = {
    11 : ' ', 12 : ' ', 13 : ' ', 
    21 : ' ', 22 : ' ', 23 : ' ', 
    31 : ' ', 32 : ' ',33 : ' ',
}

print('Welcome to the game Tic-Tac-Toe.')
print('Player 1 goes first and is X while Player 2 goes after and is O.')
print('Pick of out the nine options by inputing the select number')
print('11| 12 |13')
print('--|----|--')
print('21| 22 |23')
print('--|----|--')
print('31| 32 |33\n')

temp = True

while temp:
    print_table()

    pos = input('What is your input: ')

    if pos == 'q' or pos == 'Q':
        temp = False
        print('Game End.')
        break

    while not pos.isdigit() or int(pos) not in ticdict:
        print('INCORRECT INPUT. TRY AGAIN.')
        pos = input('What is your input: ')

    while ticdict[int(pos)] != ' ':
        print('POSITION ALREADY OCCUPIED. TRY AGAIN.')
        pos = input('What is your input: ')
    
    ticdict[int(pos)] = current_player.get_letter()
    
    if check_win(current_player):
        print_table()
        print('Congrats ' + current_player.get_name() + ', you have won.')
        break
    
    if check_tie():
        print_table()
        print('Tie Game')
        break

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    
    print('\n')

