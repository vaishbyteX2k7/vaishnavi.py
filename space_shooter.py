# import pygame
# import sys

# # ----------------------------
# # Initialize Pygame
# # ----------------------------
# pygame.init()

# # ----------------------------
# # Screen Settings
# # ----------------------------
# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Space Shooter")

# # ----------------------------
# # Colors
# # ----------------------------
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (50, 150, 255)

# # ----------------------------
# # Clock
# # ----------------------------
# clock = pygame.time.Clock()
# FPS = 60

# # ----------------------------
# # Player Settings
# # ----------------------------
# player_width = 60
# player_height = 70

# player_x = WIDTH // 2 - player_width // 2
# player_y = HEIGHT - 100

# player_speed = 7

# # ----------------------------
# # Game Loop
# # ----------------------------
# running = True

# while running:

#     # ------------------------
#     # Events
#     # ------------------------
#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#     # ------------------------
#     # Keyboard Input
#     # ------------------------
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         player_x -= player_speed

#     if keys[pygame.K_RIGHT]:
#         player_x += player_speed

#     if keys[pygame.K_UP]:
#         player_y -= player_speed

#     if keys[pygame.K_DOWN]:
#         player_y += player_speed

#     # ------------------------
#     # Keep Player Inside Screen
#     # ------------------------
#     if player_x < 0:
#         player_x = 0

#     if player_x > WIDTH - player_width:
#         player_x = WIDTH - player_width

#     if player_y < 0:
#         player_y = 0

#     if player_y > HEIGHT - player_height:
#         player_y = HEIGHT - player_height

#     # ------------------------
#     # Draw Everything
#     # ------------------------
#     screen.fill(BLACK)

#     # Spaceship Body
#     pygame.draw.polygon(
#         screen,
#         BLUE,
#         [
#             (player_x + player_width // 2, player_y),
#             (player_x, player_y + player_height),
#             (player_x + player_width, player_y + player_height)
#         ]
#     )

#     # Cockpit
#     pygame.draw.circle(
#         screen,
#         WHITE,
#         (player_x + player_width // 2, player_y + 20),
#         8
#     )

#     # ------------------------
#     # Update Screen
#     # ------------------------
#     pygame.display.update()

#     clock.tick(FPS)

# pygame.quit()
# sys.exit()








# import pygame
# import sys

# # ----------------------------
# # Initialize Pygame
# # ----------------------------
# pygame.init()

# # ----------------------------
# # Screen Settings
# # ----------------------------
# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Space Shooter - Part 2")

# # ----------------------------
# # Colors
# # ----------------------------
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (50, 150, 255)
# YELLOW = (255, 255, 0)

# # ----------------------------
# # Clock
# # ----------------------------
# clock = pygame.time.Clock()
# FPS = 60

# # ----------------------------
# # Player Settings
# # ----------------------------
# player_width = 60
# player_height = 70

# player_x = WIDTH // 2 - player_width // 2
# player_y = HEIGHT - 100

# player_speed = 7

# # ----------------------------
# # Bullet Settings
# # ----------------------------
# bullet_width = 6
# bullet_height = 15
# bullet_speed = 10

# # List to store bullets
# bullets = []

# # ----------------------------
# # Game Loop
# # ----------------------------
# running = True

# while running:

#     # ------------------------
#     # Events
#     # ------------------------
#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#         # Shoot Bullet
#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_SPACE:

#                 bullet_x = player_x + player_width // 2 - bullet_width // 2
#                 bullet_y = player_y

#                 bullets.append([bullet_x, bullet_y])

#     # ------------------------
#     # Keyboard Input
#     # ------------------------
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         player_x -= player_speed

#     if keys[pygame.K_RIGHT]:
#         player_x += player_speed

#     if keys[pygame.K_UP]:
#         player_y -= player_speed

#     if keys[pygame.K_DOWN]:
#         player_y += player_speed

#     # ------------------------
#     # Keep Player Inside Screen
#     # ------------------------
#     if player_x < 0:
#         player_x = 0

#     if player_x > WIDTH - player_width:
#         player_x = WIDTH - player_width

#     if player_y < 0:
#         player_y = 0

#     if player_y > HEIGHT - player_height:
#         player_y = HEIGHT - player_height

#     # ------------------------
#     # Move Bullets
#     # ------------------------
#     for bullet in bullets:
#         bullet[1] -= bullet_speed

#     # Remove bullets that leave the screen
#     bullets = [bullet for bullet in bullets if bullet[1] > -bullet_height]

#     # ------------------------
#     # Draw Everything
#     # ------------------------
#     screen.fill(BLACK)

#     # Draw Player
#     pygame.draw.polygon(
#         screen,
#         BLUE,
#         [
#             (player_x + player_width // 2, player_y),
#             (player_x, player_y + player_height),
#             (player_x + player_width, player_y + player_height)
#         ]
#     )

#     pygame.draw.circle(
#         screen,
#         WHITE,
#         (player_x + player_width // 2, player_y + 20),
#         8
#     )

#     # Draw Bullets
#     for bullet in bullets:
#         pygame.draw.rect(
#             screen,
#             YELLOW,
#             (bullet[0], bullet[1], bullet_width, bullet_height)
#         )

#     # ------------------------
#     # Update Screen
#     # ------------------------
#     pygame.display.update()
#     clock.tick(FPS)

# pygame.quit()
# sys.exit()









# import pygame
# import sys
# import random

# # ----------------------------
# # Initialize Pygame
# # ----------------------------
# pygame.init()

# # ----------------------------
# # Screen Settings
# # ----------------------------
# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Space Shooter - Part 3")

# # ----------------------------
# # Colors
# # ----------------------------
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (50, 150, 255)
# YELLOW = (255, 255, 0)
# RED = (255, 50, 50)

# # ----------------------------
# # Clock
# # ----------------------------
# clock = pygame.time.Clock()
# FPS = 60


# # ----------------------------
# # Player Settings
# # ----------------------------
# player_width = 60
# player_height = 70

# player_x = WIDTH // 2 - player_width // 2
# player_y = HEIGHT - 100

# player_speed = 7


# # ----------------------------
# # Bullet Settings
# # ----------------------------
# bullet_width = 6
# bullet_height = 15
# bullet_speed = 10

# bullets = []


# # ----------------------------
# # Enemy Settings
# # ----------------------------
# enemy_width = 50
# enemy_height = 50
# enemy_speed = 3

# enemies = []

# # Enemy spawn timer
# spawn_timer = 0
# spawn_delay = 40


# # ----------------------------
# # Game Loop
# # ----------------------------
# running = True

# while running:

#     # ------------------------
#     # Events
#     # ------------------------
#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False


#         # Shooting
#         if event.type == pygame.KEYDOWN:

#             if event.key == pygame.K_SPACE:

#                 bullet_x = player_x + player_width // 2 - bullet_width // 2
#                 bullet_y = player_y

#                 bullets.append([bullet_x, bullet_y])


#     # ------------------------
#     # Player Movement
#     # ------------------------
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         player_x -= player_speed

#     if keys[pygame.K_RIGHT]:
#         player_x += player_speed

#     if keys[pygame.K_UP]:
#         player_y -= player_speed

#     if keys[pygame.K_DOWN]:
#         player_y += player_speed


#     # Keep player inside screen

#     if player_x < 0:
#         player_x = 0

#     if player_x > WIDTH - player_width:
#         player_x = WIDTH - player_width

#     if player_y < 0:
#         player_y = 0

#     if player_y > HEIGHT - player_height:
#         player_y = HEIGHT - player_height



#     # ------------------------
#     # Bullet Movement
#     # ------------------------
#     for bullet in bullets:
#         bullet[1] -= bullet_speed


#     # Remove bullets outside screen
#     bullets = [
#         bullet for bullet in bullets
#         if bullet[1] > -bullet_height
#     ]



#     # ------------------------
#     # Enemy Spawning
#     # ------------------------
#     spawn_timer += 1

#     if spawn_timer >= spawn_delay:

#         enemy_x = random.randint(
#             0,
#             WIDTH - enemy_width
#         )

#         enemy_y = -enemy_height

#         enemies.append(
#             [enemy_x, enemy_y]
#         )

#         spawn_timer = 0



#     # ------------------------
#     # Enemy Movement
#     # ------------------------
#     for enemy in enemies:

#         enemy[1] += enemy_speed


#     # Remove enemies that leave screen

#     enemies = [
#         enemy for enemy in enemies
#         if enemy[1] < HEIGHT
#     ]



#     # ------------------------
#     # Drawing
#     # ------------------------
#     screen.fill(BLACK)


#     # Draw Player

#     pygame.draw.polygon(
#         screen,
#         BLUE,
#         [
#             (player_x + player_width // 2, player_y),
#             (player_x, player_y + player_height),
#             (player_x + player_width, player_y + player_height)
#         ]
#     )


#     pygame.draw.circle(
#         screen,
#         WHITE,
#         (
#             player_x + player_width // 2,
#             player_y + 20
#         ),
#         8
#     )



#     # Draw Bullets

#     for bullet in bullets:

#         pygame.draw.rect(
#             screen,
#             YELLOW,
#             (
#                 bullet[0],
#                 bullet[1],
#                 bullet_width,
#                 bullet_height
#             )
#         )



#     # Draw Enemies

#     for enemy in enemies:

#         pygame.draw.rect(
#             screen,
#             RED,
#             (
#                 enemy[0],
#                 enemy[1],
#                 enemy_width,
#                 enemy_height
#             )
#         )



#     # Update Display

#     pygame.display.update()

#     clock.tick(FPS)



# pygame.quit()
# sys.exit()










import pygame
import sys
import random

# ----------------------------
# Initialize Pygame
# ----------------------------
pygame.init()

# ----------------------------
# Screen Settings
# ----------------------------
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Part 4.1")

# ----------------------------
# Colors
# ----------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# ----------------------------
# Clock
# ----------------------------
clock = pygame.time.Clock()
FPS = 60

# ----------------------------
# Player
# ----------------------------
player_width = 60
player_height = 70

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 100

player_speed = 7

# ----------------------------
# Bullets
# ----------------------------
bullet_width = 6
bullet_height = 15
bullet_speed = 10

bullets = []

# ----------------------------
# Enemies
# ----------------------------
enemy_width = 50
enemy_height = 50
enemy_speed = 3

enemies = []

spawn_timer = 0
spawn_delay = 40

# ----------------------------
# Game Loop
# ----------------------------
running = True

while running:

    # ------------------------
    # Events
    # ------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y

                bullets.append([bullet_x, bullet_y])

    # ------------------------
    # Keyboard
    # ------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # ------------------------
    # Keep Player Inside Screen
    # ------------------------
    player_x = max(0, min(player_x, WIDTH - player_width))
    player_y = max(0, min(player_y, HEIGHT - player_height))

    # ------------------------
    # Move Bullets
    # ------------------------
    for bullet in bullets:
        bullet[1] -= bullet_speed

    bullets = [
        bullet
        for bullet in bullets
        if bullet[1] > -bullet_height
    ]

    # ------------------------
    # Spawn Enemies
    # ------------------------
    spawn_timer += 1

    if spawn_timer >= spawn_delay:

        enemy_x = random.randint(
            0,
            WIDTH - enemy_width
        )

        enemies.append(
            [enemy_x, -enemy_height]
        )

        spawn_timer = 0

    # ------------------------
    # Move Enemies
    # ------------------------
    for enemy in enemies:
        enemy[1] += enemy_speed

    enemies = [
        enemy
        for enemy in enemies
        if enemy[1] < HEIGHT
    ]

    # ------------------------
    # Bullet-Enemy Collision
    # ------------------------
    bullets_to_remove = []
    enemies_to_remove = []

    for bullet in bullets:

        bullet_rect = pygame.Rect(
            bullet[0],
            bullet[1],
            bullet_width,
            bullet_height
        )

        for enemy in enemies:

            enemy_rect = pygame.Rect(
                enemy[0],
                enemy[1],
                enemy_width,
                enemy_height
            )

            if bullet_rect.colliderect(enemy_rect):

                if bullet not in bullets_to_remove:
                    bullets_to_remove.append(bullet)

                if enemy not in enemies_to_remove:
                    enemies_to_remove.append(enemy)

    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)

    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)

    # ------------------------
    # Draw
    # ------------------------
    screen.fill(BLACK)

    # Player
    pygame.draw.polygon(
        screen,
        BLUE,
        [
            (player_x + player_width // 2, player_y),
            (player_x, player_y + player_height),
            (player_x + player_width, player_y + player_height)
        ]
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (player_x + player_width // 2, player_y + 20),
        8
    )

    # Bullets
    for bullet in bullets:
        pygame.draw.rect(
            screen,
            YELLOW,
            (
                bullet[0],
                bullet[1],
                bullet_width,
                bullet_height
            )
        )

    # Enemies
    for enemy in enemies:
        pygame.draw.rect(
            screen,
            RED,
            (
                enemy[0],
                enemy[1],
                enemy_width,
                enemy_height
            )
        )

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()