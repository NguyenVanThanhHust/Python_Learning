import os
import time

class Game:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def is_valid(self, px, py):
        if px < 0 or py < 0 or px > self.board_size or py > self.board_size:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self, ):
        # Vertical win 
        for i in range(self.board_size):
            first_value = self.current_state[0][i]
            this_line=True
            for j in range(1, self.board_size):
                if self.current_state[j][i] != first_value:
                    this_line=False
            if this_line==True and first_value != '.':
                return first_value
        
        # Horizontal win
        for i in range(self.board_size):
            first_value = self.current_state[i][0]
            this_line=True
            for j in range(1, self.board_size):
                if self.current_state[i][j] != first_value:
                    this_line=False
            if this_line==True and first_value != '.':
                return first_value

        # First diagonal win
        first_value = self.current_state[0][0]
        this_line = True
        for i in range(1, self.board_size):
            if self.current_state[i][i] != first_value:
                this_line=False
        if this_line == True and first_value != '.':
            return first_value

        # Second diagonal win
        first_value = self.current_state[0][self.board_size-1]
        this_line = True
        for i in range(1, self.board_size):
            if self.current_state[i][self.board_size-i] != this_line:
                this_line = False
        if this_line == True and first_value != '.':
            return first_value

        # If the board is not full, continue
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.current_state[i][j] == '.':
                    return None

        return '.'

    ## Minimax is implemented here
    # We are X, machine is O,
    # O wants max
    def max(self, ):
        # Possible values for max value are:
        # -1: loss
        # 0: tie 
        # 1: win 
        
        # Initialize max value as -2 
        max_value = -2

        px, py = None, None

        result = self.is_end()
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > max_value:
                        max_value = m
                        px = i 
                        py = j 
                    
                    self.current_state[i][j] = '.'
        return (max_value, px, py)

    def min(self, ):
        # Similar for max
        min_value = -2
        result = self.is_end()

        qx, qy = None, None

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < min_value:
                        min_value = m 
                        qx = i 
                        qy = j 
                    self.current_state[i][j] = '.'
        return (min_value, qx, qy)

    def play(self, ):
        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print("The winner is X!")
                elif self.result == 'O':
                    print("The winner is O!")
                elif self.result == '.':
                    print("The result is tie")
                self.initialize_game()
                return 
            
            # If it's player's turn
            if self.player_turn == 'X':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    (qx, qy) = (px, py)
                    import pdb; pdb.set_trace()
                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'X'
                self.player_turn = 'X'

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()