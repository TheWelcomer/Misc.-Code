import pygame

# Initialize Pygame
pygame.init()

# Set the size of the canvas (width, height)
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Painting")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Drawing code should go here
    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the current mouse position
    pos = pygame.mouse.get_pos()

    # Draw a circle at the mouse position
    pygame.draw.circle(screen, (0, 0, 255), pos, 10)

    # --- Go ahead and update the screen.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()