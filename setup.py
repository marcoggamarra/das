import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Grid Example")

# Grid configuration
cols = 10
rows = 8
square_width = screen.get_width() // cols
square_height = screen.get_height() // rows

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background

    # Draw grid
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col*square_width, row*square_height, square_width, square_height)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)  # White lines, 1 px thick

    pygame.display.flip()

pygame.quit()
