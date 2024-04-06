
### LIBRARIES ###
import numpy as np
import pygame

class Robot:

    def __init__(self, initial_x, initial_y, R=3, L=25):
        ### ROBOT PARAMETERS ###        
        # wheel radius in px
        self.R = R
        # Distance between the wheel centers in px
        self.L = L
        #### POSE ###
        # x, y, angle
        self.position = [float(initial_x), float(initial_y), float(0)]        
        ### CONTROLS ###
        # Left wheel velocity
        self.w_l = 0.0
        # Right wheel velocity
        self.w_r = 0.0         
        ### GRAPHICS ###
        # Original Robot image
        self.robot_design = pygame.image.load('design/robot.png').convert_alpha() 
        # Rotated Robot
        self.rotated_robot = self.robot_design
        self.rect = self.rotated_robot
        ##### INDICATIONS 
        self.stop_signal = False  
        ##### LASER SENSOR
        self.num_points = 360
        self.max_dist = 300             
    
    def draw(self, surface):
        # Drawing robot with clean rotation
        surface.blit(self.rotated_robot,
                      (self.position[0] - self.rotated_robot.get_width() // 2,
                        self.position[1] - self.rotated_robot.get_height() // 2))      

    def move(self, dt, event=None):
        if not self.stop_signal:
            # Only execute this if stop_signal is False
            if event is not None:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Turn right
                        self.w_l += 1.0
                        self.w_r -= 1.0 
                    if event.key == pygame.K_LEFT:
                        # Turn left
                        self.w_l -= 1.0
                        self.w_r += 1.0 
                    if event.key == pygame.K_UP:
                        # Acelerate
                        self.w_l += 1.0
                        self.w_r += 1.0
                    if event.key == pygame.K_DOWN:
                        # Desacelerate
                        self.w_l -= 1.0
                        self.w_r -= 1.0
                    if event.key == pygame.K_SPACE:
                        self.w_l = 0.0
                        self.w_r = 0.0
        else:
            # If stop_signal is True -> Stop robot
            self.w_l = 0.0
            self.w_r = 0.0

        # Equations
        # x
        self.position[0] += ((self.w_l + self.w_r)/2) * np.cos(self.position[2]) * dt              
        # y
        self.position[1] -= ((self.w_l + self.w_r)/2) * np.sin(self.position[2]) * dt
        # theta
        self.position[2] += (self.w_r - self.w_l) / self.L * dt  
        # Rotation
        self.rotated_robot = pygame.transform.rotozoom(self.robot_design, np.degrees(self.position[2]), 1)
        self.rect = self.rotated_robot.get_rect(center=(self.position[0], self.position[1]))
        
    def laser_sensor(self, surface):        
        for i in range(self.num_points):
            angle = np.radians(i)
            x = self.position[0] + self.max_dist * np.cos(angle)
            y = self.position[1] + self.max_dist * np.sin(angle)
            pygame.draw.line(surface, (0,255,0), self.position[:2], (x,y))

        
        






   

