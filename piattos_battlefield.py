import pygame
import random

pygame.init()

#window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Piattos Battlefield")

#images
piattos_blue = pygame.image.load("C:\\Users\\Railyn Izza\\Downloads\\piattos_blue.png").convert_alpha()
piattos_green = pygame.image.load("C:\\Users\\Railyn Izza\\Downloads\\piattos_green.png").convert_alpha()
knife_image = pygame.image.load("C:\\Users\\Railyn Izza\\Downloads\\pangmalakasang_axe.png").convert_alpha()
explosion_image = pygame.image.load("C:\\Users\\Railyn Izza\\Downloads\\explosion.png").convert_alpha()

#resizing
piattos_blue = pygame.transform.scale(piattos_blue, (100, 100))
piattos_green = pygame.transform.scale(piattos_green, (100, 100))
knife_image = pygame.transform.scale(knife_image, (50, 50))
explosion_image = pygame.transform.scale(explosion_image, (200, 200))

#pagalawin mga piattos
image_width, image_height = piattos_blue.get_size()
piattos_blue_x = random.randint(0, width - image_width)
piattos_blue_y = random.randint(0, height - image_height)
piattos_blue_dx, piattos_blue_dy = 5, 5

#piattos green pagalawin pa rin
image_width, image_height = piattos_green.get_size()
piattos_green_x = random.randint(0, width - image_width)
piattos_green_y = random.randint(0, height - image_height)
piattos_green_dx, piattos_green_dy = -5, -5

#knife
knife_x = random.randint(0, width - 50)
knife_y = random.randint(0, height - 50)
knife_acquired = None

explosion = False
explosion_x, explosion_y = 0, 0
winner_image = None

#main loop
running = True
while running:
    screen.fill((0, 0, 0))
    if not explosion:
        piattos_blue_x += piattos_blue_dx
        piattos_blue_y += piattos_blue_dy
        piattos_green_x += piattos_green_dx
        piattos_green_y += piattos_green_dy

        if piattos_blue_x <= 0 or piattos_blue_x + image_width >= width:
            piattos_blue_dx *= -1
        if piattos_blue_y <= 0 or piattos_blue_y + image_height >= height:
            piattos_blue_dy *= -1
        if piattos_green_x <= 0 or piattos_green_x + image_width >= width:
            piattos_green_dx *= -1
        if piattos_green_y <= 0 or piattos_green_y + image_height >= height:
            piattos_green_dy *= -1

        #draw images
        screen.blit(piattos_blue, (piattos_blue_x, piattos_blue_y))
        screen.blit(piattos_green, (piattos_green_x, piattos_green_y))

        #knife
        if knife_acquired is None:
            screen.blit(knife_image, (knife_x, knife_y))
        if knife_acquired is None:
            if pygame.Rect(piattos_blue_x, piattos_blue_y, image_width, image_height).colliderect(pygame.Rect(knife_x, knife_y, 50, 50)):
                knife_acquired = "piattos_blue"
            elif pygame.Rect(piattos_green_x, piattos_green_y, image_width, image_height).colliderect(pygame.Rect(knife_x, knife_y, 50,50)):
                knife_acquired = "piattos_green"

        #may nakakuha na ng knife
        if knife_acquired == "piattos_blue":
            screen.blit(knife_image, (piattos_blue_x + image_width - 20, piattos_blue_y + image_height // 2 - 10))
        elif knife_acquired == "piattos_green":
            screen.blit(knife_image, (piattos_green_x + image_width - 20, piattos_green_y + image_height // 2 - 10))

        #gripo time
        if knife_acquired == "piattos_blue" and pygame.Rect(piattos_blue_x, piattos_blue_y, image_width, image_height).colliderect(pygame.Rect(piattos_green_x, piattos_green_y, image_width, image_height)):
            explosion = True
            explosion_x, explosion_y = piattos_green_x, piattos_green_y
            winner_image = piattos_blue
        elif knife_acquired == "piattos_green" and pygame.Rect(piattos_green_x, piattos_green_y, image_width, image_height).colliderect(pygame.Rect(piattos_blue_x, piattos_blue_y, image_width, image_height)):
            explosion = True
            explosion_x, explosion_y = piattos_blue_x, piattos_blue_y
            winner_image = piattos_green

    #explosion
    else:
        screen.blit(explosion_image, (explosion_x - 40, explosion_y - 40))
        if winner_image:
            screen.blit(winner_image, (explosion_x + 50, explosion_y + 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
