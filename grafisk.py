import pygame
import random
import math

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))

particles = [] # [[x, y], [vel_x, vel_y], ttl]

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))




    for i in range(5):
        particles.append([[pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]], [random.randint(-5, 5), random.randint(-5, 5)], 10])

    for particle in particles: 
        pygame.draw.circle(screen, (0, 0, 0), particle[0], int(particle[2]))
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]    
        particle[2] -= 0.5
        if particle[2] <= 0:
            particles.remove(particle)
    
    # Update the display
    pygame.display.flip()

    clock.tick(30)

pygame.quit()