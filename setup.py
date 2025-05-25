import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RPG Visual Story")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background
    pygame.display.flip()

pygame.quit()
