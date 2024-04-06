import pygame

class Utils:
    
    def __init__(self, obstacles, robot):
        # Obstacles
        self.obstacles = obstacles       
        self.robot = robot

    def collision(self, robot):
        if robot.colliderect(self.obstacles.left_wall):            
            self.robot.stop_signal = True
        elif robot.colliderect(self.obstacles.top_wall):
            self.robot.stop_signal = True
        elif robot.colliderect(self.obstacles.right_wall):
            self.robot.stop_signal = True
        elif robot.colliderect(self.obstacles.bottom_wall):
            self.robot.stop_signal = True
        