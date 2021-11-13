import pygame
from pygame.locals import *
import time
import random
from math import e

SIZE = 50

#########################################################################################
class Rocket:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("newRocket.jpg").convert()
        rocket = pygame.transform.rotate(self.image, 270)
        self.rocket = rocket
        self.parent_screen = parent_screen
        self.x = 0
        self.y = random.randint(20,670)


    def draw(self, x,y):
        self.parent_screen.blit(self.rocket, (x, y))
        pygame.display.flip()

    def move(self):
        self.x += SIZE-25
        self.draw(self.x, self.y)

    def reset(self):
        self.x = 0
        self.y = random.randint(20,670)
        self.draw(self.x, self.y)
            
 #####################################################################################           
class Shield:
    def __init__(self, parent_screen):
        self.sheild = pygame.image.load("newShield.jpg").convert()
        self.parent_screen = parent_screen
        self.rocket = Rocket(self.parent_screen)
        self.x = 600
        self.y = 400

    def draw(self):
        self.parent_screen.blit(self.sheild, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.draw()
        self.y -= 20
        

    def move_down(self):
        self.draw()
        self.y += 20

#############################################################################################
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((700,700))
        self.shield = Shield(self.surface)
        self.rocket = Rocket(self.surface)
        self.score = 0

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
             if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
        
    def out_of_bounds(self):
        if self.rocket.x >= 690:
            return True
        return False
    def display_score(self):
        self.surface.fill((239,241,239, 0))
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: " + str(self.score), True, (0, 0, 0))
        self.surface.blit(score, (50, 50))

    def display_final(self):
        self.surface.fill((239,241,239, 0))
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Your Final Score Was: " + str(self.score), True, (0, 0, 0))
        string = font.render(f'Press Enter to Play again', True, (0,0,0))
        self.surface.blit(score, (350, 350))
        self.surface.blit(string,(350, 450))
        pygame.display.flip()

    def play(self):
        self.surface.fill((239,241,239, 0))
        self.display_score()
        self.shield.draw()
        self.rocket.move()
        pygame.display.flip()
           

        if self.is_collision(self.rocket.x, self.rocket.y, self.shield.x, self.shield.y):
            self.rocket.reset()
            self.score += 1

        if self.out_of_bounds():
            raise "Game Over"
    def reset(self):
        self.score = 0
        self.rocket.x = 0

    def run(self):
        running = True
        pause = False
    
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.rocket.draw(self.rocket.x, self.rocket.y)
                            self.shield.move_up()
                        
                        if event.key == K_DOWN:
                            self.rocket.draw(self.rocket.x, self.rocket.y)
                            self.shield.move_down()
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()  
            except Exception as e:
                self.display_final()
                pause = True
                self.reset()
            if self.score < 5:            
                time.sleep(0.2)
            elif self.score >= 5 and self.score < 10:
                time.sleep(0.15)
            else:
                time.sleep(.1)

##################################################################################################################
if __name__ == "__main__":
    game = Game()
    game.run()


