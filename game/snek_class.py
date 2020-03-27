import numpy as np

class snek:
    def __init__ (self, start_location, snek_id, start_size = 1):
        self.head_loc = start_location #vector (x,y)
        self.size = np.array([start_size]) #vector T long containing size data
        self.pos = np.array([start_location]) # T x 2 matrix storing pos data
        self.id = snek_id
        self.alive = True
        self.info = {'id':self.id,'pos':self.pos, 'size':self.size}

    def move (self, move_array):
        
        if np.argmax(move_array) == 0:
            dp = np.array([0,1])

        elif np.argmax(move_array) == 1:
            dp = np.array([-1,0])

        elif np.argmax(move_array) == 2:
            dp = np.array([0,-1])

        elif np.argmax(move_array) == 3:
            dp = np.array([1,0])
        

        new_pos = np.add(self.pos[0], dp)

        self.pos = np.append(np.array([new_pos]), self.pos, axis= 0)

    def step(self, board_info, move_array):
        if board_info[self.id] >= 0:
            self.move(move_array)

            dl= 0

            if board_info[self.id] == 1:
                dl = 1
    
            new_size = self.size[0]+dl
            self.size = np.append(new_size, self.size)
        else:
            pass
        self.info = {'id':self.id,'pos':self.pos, 'size':self.size}