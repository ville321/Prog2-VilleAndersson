import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.time_duration = 5
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.state = "start" # för att göra en startskärm, spel och game over
        self.font = pygame.font.Font(None, 74)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.state == "start" or self.state == "game over":
                        self.state = "playing"
                        self.score = 0
                        self.time_duration = 5
                elif event.type == pygame.MOUSEBUTTONDOWN and self.state == "playing":
                    for circle in circles:
                        if circle.is_clicked(event.pos):
                            particle_system.add_particles(circle.position)
                            circles.remove(circle)
                            self.score += 1
                            circles.append(Circle((random.randint(50, 750), random.randint(50, 550))))
                            self.time_duration = 5 
                            break

            self.screen.fill((255, 255, 255))

            if self.state == "start":
                self.write_text("'ENTER' för att starta", self.width / 2, self.height / 2)
            elif self.state == "game over":
                self.write_text("Du dog, 'ENTER' för att börja om", self.width / 2, self.height / 2)
            elif self.state == "playing":
                self.write_text(f"{self.score}", 50, 50)
                self.write_text(f"{self.time_duration:.2f}", self.width - 75, 50)
                self.time_duration -= 0.01
                if self.time_duration <= 0: 
                    self.state = "game over"
                for circle in circles:
                    circle.update(self.width, self.height)
                    circle.draw(self.screen)

                particle_system.update()
                particle_system.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def write_text(self, text, x, y):
        rendered_text = self.font.render(text, True, (0, 0, 0))
        text_rect = rendered_text.get_rect(center=(x, y))
        self.screen.blit(rendered_text, text_rect)

class Particle:
    def __init__(self, position, velocity, ttl):
        self.position = list(position)
        self.velocity = velocity
        self.ttl = ttl # Time to live. Så att partiklarna försvinner efter en viss tid

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.ttl -= 0.5

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, int(self.ttl))

class ParticleSystem:
    def __init__(self):
        self.particles = [] # En lista som håller partiklarna

    def add_particles(self, position):
        for i in range(20):
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

    def update(self, width, height):
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

particle_system = ParticleSystem()
circles = []
for i in range(5):
    circles.append(Circle((random.randint(50, 750), random.randint(50, 550))))

Game().run()