import pygame
import random

pygame.init()

class Particle:
    def __init__(self, position, velocity, ttl):
        self.position = list(position)
        self.velocity = velocity
        self.ttl = ttl #vet inte om det är korrekt men använder ttl (time to live) som begrepp för att hålla koll på partikelns livslängd.

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.ttl -= 0.5

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, int(self.ttl))

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particles(self, position):
        for _ in range(20):
            velocity = [random.uniform(-5, 5), random.uniform(-5, 5)]
            self.particles.append(Particle(position, velocity, 10))

    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.ttl <= 0: 
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)

class Circle:
    def __init__(self, position, radius=20):
        self.position = list(position)
        self.radius = radius
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        if self.position[0] - self.radius < 0 or self.position[0] + self.radius > width:
            self.velocity[0] *= -1
        if self.position[1] - self.radius < 0 or self.position[1] + self.radius > height:
            self.velocity[1] *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)

    def is_clicked(self, mouse_pos):
        distance = ((self.position[0] - mouse_pos[0]) ** 2 + (self.position[1] - mouse_pos[1]) ** 2) ** 0.5
        return distance < self.radius

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

particle_system = ParticleSystem()
circles = [Circle((random.randint(50, 750), random.randint(50, 550))) for _ in range(5)]

clock = pygame.time.Clock()
score = 0
time_duration = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for circle in circles:
                if circle.is_clicked(event.pos):
                    particle_system.add_particles(circle.position)
                    circles.remove(circle)
                    score += 1
                    circles.append(Circle((random.randint(50, 750), random.randint(50, 550))))
                    time_duration = 5 
                    break

    screen.fill((255, 255, 255))

    # Minskar tiden
    time_duration -= 0.01

    for circle in circles:
        circle.update()
        circle.draw(screen)

    particle_system.update()
    particle_system.draw(screen)

    # Texter på skärmen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    timer_text = font.render(f"Tid: {time_duration}", True, (0, 0, 0))
    screen.blit(timer_text, (width - 150, 10))

    if time_duration <= 0:
        running = False  # Avslutar spelet

    pygame.display.flip()
    clock.tick(60)

pygame.quit()