import pygame


# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
icon = pygame.image.load('ufo.png')
title = "Space Invaders"

pygame.display.set_caption(title)
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerimg, (x, y))

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystoke has been released")

    playerX += playerX_change

    player(playerX, playerY)
    pygame.display.update()
