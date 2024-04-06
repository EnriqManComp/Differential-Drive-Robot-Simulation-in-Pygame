
### LIBRARIES ###
import pygame
from robot import Robot
from obstacles import Obstacles
from utils import Utils
class enviroment:

    def __init__(self):
        # Initialise pygame
        pygame.init()
        # Set window
        self.screen = pygame.display.set_mode((800, 600))
        # FPS controler
        self.clock = pygame.time.Clock()
        # Initialising robot
        self.robot = Robot(initial_x=100, initial_y=100)     
        # Obstacle object
        self.obstacles = Obstacles(self.screen)
        # Utils
        self.utils = Utils(self.obstacles, self.robot)  

    def run(self): 
        # Running variable   
        running = True
        dt = 0
        last_time = pygame.time.get_ticks()        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                # Check move instructions
                self.robot.move(dt, event)
            # differential time
            dt = (pygame.time.get_ticks()-last_time) / 1000            
            last_time = pygame.time.get_ticks()            
            # Background color
            self.screen.fill((0,0,0))
            # Movement update
            self.robot.move(dt)
            # Draw walls
            self.obstacles.render_walls()
            # Draw robot            
            self.robot.laser_sensor(self.screen)
            self.robot.draw(self.screen) 
                       
            self.utils.collision(self.robot.rect)
            # Updating display 60 Hz                        
            pygame.display.update()
            self.clock.tick(60)            

        pygame.quit()

enviroment().run()