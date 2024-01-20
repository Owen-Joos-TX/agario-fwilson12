import pygame, sys, random


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("agar.io")



clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, player_radius):
        self.radius = random.randint(player_radius + 1, 2 * player_radius)  # Random radius
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
        self.speed = 1 / self.radius  # Inversely proportional speed
        self.direction = random.uniform(0, 2 * math.pi)  # Random heading
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)

    def move(self):
        # Move in a straight line, reflect off boarder
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

        # Reflect off boarder
        if self.x < 0 or self.x > self.screen_width:
            self.direction = math.pi - self.direction
        if self.y < 0 or self.y > self.screen_height:
            self.direction = -self.direction

    def collision_detector(self, other_object):
        distance = self.distance(self.x, self.y, other_object.x, other_object.y)
        return distance < (self.radius + other_object.radius)

    def grow(self, absorbed_object_radius):
        self.radius += absorbed_object_radius
        self.speed = 1 / self.radius  # Update speed proportionally

    @staticmethod # using a static method here because it doestn have access to instance-specific data so this is just a clearner way of doing this
    def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    

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
