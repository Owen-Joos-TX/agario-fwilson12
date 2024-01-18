import pygame, sys, random


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("agar.io")



clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, number, x, y):
        super(Enemy, self).__init__()
        self.id = number
        self.radius = random.randint(15,35)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.self.circle(self.circle, (255, 0, 0, 128), (self.radius, self.radius), self.radius)
        self.colors = ['red','orange','yellow','green','light blue','blue','purple']
        self.colors = random.choice(self.colors)
        self.speed = 100 * 1/self.radius
        self.deltax = self.speed
        self.deltay = self.speed
        self.rect = self.get_rect(center = (x,y))

    def create(self):
        pass
    def move(self):
        pass

    

class Food(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Food, self).__init__()
        self.radius = 10
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.randint(15,785),random.randint(15, 585)))


meals = pygame.sprite.Group()
for num in range(20):
    meals.add(Food("red"))


running = True
while running:

    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")


    meals.draw(screen)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
