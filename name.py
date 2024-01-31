
class player():
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
    
    def __repr__(self):
        return self.name + '(' + self.letter + ')'

    def get_letter(self):
        return self.letter

player1 = player('Player 1', 'X')
player2 = player('Player 2', 'O')
current_player = player1

pos11 = ' '
pos12 = ' '
pos13 = ' '
pos21 = ' '
pos22 = ' '
pos23 = ' '
pos31 = ' '
pos32 = ' '
pos33 = ' '

print('Welcome to the game Tic-Tac-Toe.')
print('Player 1 goes first and is X while Player 2 goes after and is O.')


print('  |   |  ')
print('--|---|--')
print('  |   |  ')
print('--|---|--')
print('  |   |  ')
print('Current Player: ' + str(current_player))




k = 'X'
if ((pos11 == k and pos12 == k and pos13 == k) 
    or (pos21 == k and pos22 == k and pos23 == k) 
    or (pos31 == k and pos32 == k and pos33 == k) 
    or (pos11 == k and pos21 == k and pos31 == k) 
    or (pos12 == k and pos22 == k and pos32 == k) 
    or (pos13 == k and pos23 == k and pos33 == k) 
    or (pos11 == k and pos22 == k and pos33 == k) 
    or (pos13 == k and pos22 == k and pos31 == k)):
    k = 'O'

