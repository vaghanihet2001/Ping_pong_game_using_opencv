from classes.ball import Ball
from classes.bat import Bat
import numpy as np
import cv2

class GameManager():
    
    def __init__(self,width,height,border = 5) -> None:
        self.border = border
        self.width = width
        self.height = height
        self.time = 0
        self.ground = np.zeros((self.height,self.width,3))
        self.score = 0
        self.move = 1
        self.speed = 100
        
    def draw_boder(self):
        # upper border
        self.ground[:self.border,:,:] = np.ones((self.border,self.width,3))*255
        # left border
        self.ground[:,:self.border,:] = np.ones((self.height,self.border,3))*255
        # bottom border
        self.ground[-(self.border):,:,:] = np.ones((self.border,self.width,3))*255
        # right border
        self.ground[:,-(self.border):,:] = np.ones((self.height,self.border,3))*255
        center = self.ground.shape[1]//2
        self.ground[:,center-3:center+3,:] = np.ones((self.height,6,3))
        
    def start(self):
    
        bat = Bat(self.width,self.height,self.border)
        ball = Ball(self.width, self.height,self.border)
        image = bat.spown(self.ground)
        image = ball.spown(self.ground)
       
        while True:
            image = self.ground.copy()
            image = cv2.putText(image,"Time : "+str(self.time),(50,50),1,1,(255,255,255))
            image = cv2.putText(image,"Score : "+str(self.score),(50,100),1,1,(255,255,255))
            self.time+=1
            # if bat.pos == ball.pos:
            #     bat.length += 1
            #     image = ball.spown(image)
            #     self.point_score()
            # else:
            image = ball.update(image)
            # print(snake.pos ,prey.pos)
            image , status  = bat.update(image,self.move)
            cv2.imshow("Snake Game",image)
            # if not status:
            #     break
            key = cv2.waitKeyEx(self.speed)
        
            if key == ord('w') or key == 2490368:
                self.move = 0
            elif key == ord('s') or key == 2621440: 
                self.move = 1
            elif key == 27: # Esc
                break
        status = True
        if not status:
            text = "Game Over"
        else:
            text = "Quiting Game?"
        image = cv2.putText(image,text,(image.shape[1]//2,image.shape[0]//2),1,2,(255,255,255),2)
        cv2.imshow("Snake Game",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
                
            
        
    def point_score(self):
        self.score += 1
        self.speed -= 5 # less speed value == more speed
        