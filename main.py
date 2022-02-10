import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.jpg")

# Backgroung sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and icon
icon = pygame.image.load('ufo.png')
title = "Space Invaders"

pygame.display.set_caption(title)
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 500
playerX_change = 0

# Enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.6)
    enemyY_change.append(64)

# Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 500
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('04B_20__.TTF', 16)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('04B_20__.TTF', 32)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY) -> bool:
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) +
                         math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(pygame.transform.scale(background, (800, 600)), (0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_SPACE and bullet_state is "ready":
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()

                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystoke has been released")

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy loop
    for i in range(num_of_enemy):
        # Game over
        if enemyY[i] > 460:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break

        #Enemy moviment
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.6
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.6
            enemyY[i] += enemyY_change[i]
        
        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()

            bulletY = playerY
            bulletX = playerX
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # Bullet moviment
    if bulletY < 0:
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
