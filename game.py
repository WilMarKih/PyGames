import pygame,sys

class Game:
    def __init__(self) -> None:
    
        pygame.init()
        # initialization of the pygame package 

        pygame.display.set_caption("The Black Esper")
        # Setting the name of the pop-up window

        self.screen = pygame.display.set_mode((640,480))
        # set_mode() operator explains on the resolution of the screen 

        self.clock = pygame.time.Clock()
        # force the game to run at defined fps to limit killing my potato pc

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        # loading images 

        self.img_pos = [160, 260] # image position
        self.movement  = [False, False]

    def run(self):
        while True:
            self.screen.blit(self.img, (self.img_pos))
            # adding the cloud image onto the screen 
             
            for event in pygame.event.get(): 
            # get user input and avoids the window from freezing
                if event.type == pygame.QUIT:
                    pygame.quit() # hard code the functionality to close the window
                    sys.exit() # exit the app
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True


        # initializing an infinite loop 
            pygame.display.update() # prevents the called screen to be always black
            self.clock.tick(30) # for 30fps

Game().run()
# let's initialize the game 