import pygame
from button import Button
import os


# Global Variables
TITLE = "Snakes and Ladders"

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 626

IMAGE_DIRECTORY = "images/"

FPS = 60  # frames per second

FONT_SIZE = 36

# Colors
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()   

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


class GameManage:
    START_SCREEN = 'start'
    GAME_SCREEN = 'game'
    WIN_SCREEN = 'win'

    def __init__(self):
        self.curr_screen = GameManage.START_SCREEN
    
    def change_screen(self, screen):
        self.curr_screen = screen
    
    def run(self):
        while True:
            match self.curr_screen:
                case GameManage.START_SCREEN: self.start_screen()
                case GameManage.GAME_SCREEN: self.game_screen()
                case GameManage.WIN_SCREEN: self.win_screen()
    
    def start_screen(self):
        background = pygame.image.load(os.path.join(IMAGE_DIRECTORY, 'background.png'))
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        snake_ladder_icon = pygame.image.load(os.path.join(IMAGE_DIRECTORY, 'snake_ladder_icon.png'))
        snake_ladder_icon = pygame.transform.scale(snake_ladder_icon, (600, 400))

        play_button = Button(
            (SCREEN_WIDTH//2 - 100), 400,
            "Play",
            color=(50, 200, 50),
            hover_color=(40, 180, 40),
            click_color=(30, 160, 30)
        )

        quit_button = Button(
            (SCREEN_WIDTH//2 - 100), 475,
            "Quit",
            color=(200, 50, 50),
            hover_color=(180, 40, 40),
            click_color=(160, 30, 30)
        )

        while self.curr_screen == GameManage.START_SCREEN:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                play_button.check_events(event)
                quit_button.check_events(event)
                
                if play_button.is_clicked(event):
                    self.change_screen(GameManage.GAME_SCREEN)
                
                if quit_button.is_clicked(event):
                    pygame.quit()
                    exit()

            screen.blit(background, (0, 0))
            screen.blit(snake_ladder_icon, ((SCREEN_WIDTH-600)//2, 0))

            play_button.draw(screen)
            quit_button.draw(screen)

            pygame.display.update()
            clock.tick(FPS)
    
    def game_screen(self):
        while self.curr_screen == GameManage.GAME_SCREEN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill(WHITE)

            pygame.display.update()
            clock.tick(FPS)

    def win_screen(self):
        pass

game = GameManage()
game.run()
