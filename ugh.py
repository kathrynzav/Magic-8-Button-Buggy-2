import sys
import random
import pygame

pygame.init()

responses = ["Sit on it. Literally.", "Concentrate and ask again", "That sounds best", "Are you sure about that?", "What does your heart say?", "No way dude", "Uh hell yeah!", "Yick", "Yeet it", "Drink some Shrek juice", "How tf would I know"]
screen_width = 820
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Magic 8 Button")
mouse_pos = pygame.mouse.get_pos()
mainButton = pygame.Rect(0, 0, 100, 100)

def make_Button(x, y, buttonText):
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
        if mainButton.collidepoint(mouse_pos):
            print(random.choice(responses))
            mouse_pos = (100, 100)

        pygame.draw.rect(screen, (255, 0, 0), mainButton)
        mainButton.center = (screen_width / 2, screen_height / 2)
        pygame.display.update()
