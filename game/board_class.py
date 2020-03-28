from game.snek_class import snek
import os
import numpy as np
import math
import random



class ai_tester:
    def __init__(self, brain =None):
        pass

    def make_move(self,board):
        print(board)
        print()
        resp = input("Move: ")
        if resp == 'd':
            return [1,0,0,0]
        elif resp == 'w':
            return [0,1,0,0]
        
        elif resp == 'a':
            return [0,0,1,0]
        elif resp == 's':
            return [0,0,0,1]
        


class board:
    def __init__(self, snek_numb, board_size = (10,10)):
        self.board_size = board_size
        self.sneks = []
        self.apple_eaten = True
        self.apple_cords = [0,0]
        self.board_info = {}
        for i in range(snek_numb):
            numb_space = board_size[0]*board_size[1]
            distance = numb_space/(snek_numb+1)
            place = distance*(i+1)
            pos = [ math.floor(place/board_size[0])+1, math.floor(place%board_size[0])]
            self.sneks.append(snek(np.array(pos),str(i)))
            self.board_info[str(i)] = 0
        self.board = np.zeros(board_size, dtype=int)


    def make_board(self):
        self.board = np.zeros(self.board_size, dtype=int) 
        self.killed = []
        self.place_snake()
        self.check_colision_snake()
        self.kill_player()
        self.place_apple()
        self.check_colision_apple()

    

    def place_snake(self):
        for snek in self.sneks:
            size = snek.info['size']
            pos = snek.info['pos']
            current_pos = pos[:size[0]]
            for pos in current_pos:
                try:
                    self.board[pos[0]][pos[1]] += -1
                except IndexError:
                    print('y')
                    id = snek.info['id']
                    self.killed.append(id)
    

    def check_colision_snake(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] <-1:
                    for snek in self.sneks:
                        if snek.info['pos'][0][0] == i and snek.info['pos'][0][1] == j: 
                            id = snek.info['id']
                            self.killed.append(id)  
    

    def check_colision_apple(self):
        for snek in self.sneks:
            pos = snek.info['pos'][0]
            if pos[0] == self.apple_cords[0] and pos[1] == self.apple_cords[1]:
                self.board_info['id'] = 1
                self.apple_eaten = True
                snek.info['size'] +=1
                self.board[pos[0]][pos[1]] = -1


    def kill_player(self):
        for id in self.killed:
            for snek in self.sneks:
                if snek.info['id'] == id:
                    self.sneks.remove(snek)



    def place_apple(self):
        if self.apple_eaten:
            x = random.randint(0, self.board_size[0]) -1
            y = random.randint(0, self.board_size[1]) -1
            self.apple_cords = [x,y]
            
            
            if self.board[self.apple_cords[0]][self.apple_cords[1]] < 0:
                self.place_apple()
            
        self.board[self.apple_cords[0]][self.apple_cords[1]] = 1
        self.apple_eaten = False
        

    def step(self, ai_object):
        ai = ai_object
        self.make_board()
        for snek in self.sneks:
            self.make_board()
            print('Player: ' + snek.info['id'])
            pos = snek.info['pos'][0]
            render = self.board
            render[pos[0]][pos[1]] = 2
            move = ai.make_move(render)
            snek.step(self.board_info, move)


