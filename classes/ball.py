import cv2
import numpy as np

class Ball():
    
    def __init__(self,width,height,unit = 5) -> None:
        self.unit = unit
        self.min_x_cord = unit
        self.min_y_cord = unit
        self.max_x_cord = width - (unit*2)
        self.max_y_cord = height - (unit*2)
        self.pos = None
        self.current_pos = None
        self.direction = 1 # left=0 , right=1
        self.slope = 0.45
        self.angle = 0
        self.coff = 0
        self.speed = 1
        
    def spown(self,image):
        # x = np.random.randint(self.min_x_cord,self.max_x_cord)
        # y = np.random.randint(self.min_y_cord,self.max_y_cord)
        x = image.shape[1]//2
        y = image.shape[0]//2
        image = cv2.circle(image.copy(),(x,y),self.unit//2,(0,0,255),self.unit//2)
        self.pos = [x//self.unit,y//self.unit]
        self.current_pos = [x,y]
        print("spown",self.pos,self.current_pos)
        self.is_alive = True
        return image
    
    def cal_line(self,image):
        x_start , y_start =  self.current_pos
        # self.angle 
        # self.coff = 
        
    def update(self,image):
        x_old,y_old = self.current_pos
        if self.direction == 0:
            x_new = x_old - self.speed
        else:
            x_new = x_old + self.speed
        print((np.tanh(self.slope)*180)/3.14,self.coff)
        y_new = int(self.slope*x_new) + self.coff
        print(x_new,y_new)
        
        if x_new >= self.min_x_cord and x_new <= self.max_x_cord and y_new >= self.min_y_cord and y_new <= self.max_y_cord:
            image = cv2.circle(image.copy(),(x_new,y_new),self.unit//2,(0,0,255),self.unit//2)
            self.current_pos = [x_new,y_new]
        return image