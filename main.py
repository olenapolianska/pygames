import pygame

pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

fon_image = pygame.image.load("background.png")
fon_image = pygame.transform.scale(fon_image, (800, 500))
sprite1 = pygame.image.load("sprite1.png")
sprite1 =  pygame.transform.scale(sprite1, (50, 50))
sprite2 = pygame.image.load("sprite2.png")
sprite2 =  pygame.transform.scale(sprite2, (50, 50))
x1, y1= 50, 50
x2, y2= 40, 70
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        if x1 + 5 < 800 - 50:
            x1 += 5
    if keys[pygame.K_s]:
        if x1 - 5 > 0 :
            x1 -= 5
    if keys[pygame.K_x]:
        if y1 + 5 < 500 - 50:
            y1 += 5
    if keys[pygame.K_e]:
        if y1 - 5 > 0 :
            y1 -= 5

    if keys[pygame.K_RIGHT]:
        if x2 + 5 < 800 - 50:
            x2 += 5
    if keys[pygame.K_LEFT]:
        if x2 - 5 > 0:
            x2 -= 5
    if keys[pygame.K_DOWN]:
        if y2 + 5 < 500 - 50:
            y2 += 5
    if keys[pygame.K_UP]:
        if y2 - 5 > 0:
            y2 -= 5

    window.blit(fon_image, [0, 0])
    window.blit(sprite1, [x1, y1])
    window.blit(sprite2, [x2, y2])
    pygame.display.flip()
    fps.tick(60)
