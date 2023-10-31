import cv2
import numpy as np

class Bat():
    
    def __init__(self,width,height,unit) -> None:
        self.length = 5
        self.body = []
        self.score = 0
        self.unit = unit
        self.player1_x_cord = unit
        self.min_y_cord = unit
        self.player2_x_cord = width-(unit*2)
        self.max_y_cord = height-(unit*2)-self.length*unit
        self.pos = None
        self.is_alive = True
        
    def spown(self,image):
        # x = np.random.randint(self.player1_x_cord,self.player2_x_cord)
        x1 = self.unit
        x2 = image.shape[1] - self.unit*2
        
        y = np.random.randint(self.min_y_cord,self.max_y_cord)
        image = cv2.rectangle(image.copy(),(x1,y),(x1+self.unit,y+self.unit*self.length),(0,255,0),-1)
        image = cv2.rectangle(image,(x2,y),(x2+self.unit,y+self.unit*self.length),(0,255,0),-1)
        # self.body.append([x,y])
        self.pos = [y,y]
        return image
    
    def update(self,image,move):
        cp = self.pos
        if move == 0 : # top
            np = [cp[0],cp[1]-self.unit]
        elif move == 1: # down
            np = [cp[0],cp[1]+self.unit]
        
        if np[1] <= self.max_y_cord and np[1] >= self.min_y_cord :
            self.pos = np
        
        image  = cv2.rectangle(image,(self.player1_x_cord,self.pos[1]),(self.player1_x_cord+self.unit,self.pos[1]+self.unit*self.length),(0,255,0),-1)
        image  = cv2.rectangle(image,(self.player2_x_cord,self.pos[1]),(self.player2_x_cord+self.unit,self.pos[1]+self.unit*self.length),(0,255,0),-1)

        return image , True