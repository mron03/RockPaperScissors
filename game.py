import pygame
import random

def startGame(VALUES):
    
    pygame.init()

    WIDTH = 1500
    HEIGHT = 1000
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ROCK PAPER SCISSOR")
    clock = pygame.time.Clock()


    class Image:
        def __init__(self, x, y, image, speed, id):
            self.x = x
            self.y = y
            self.image = image
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.speed = speed
            self.dx = random.choice([-1, 1]) * self.speed
            self.dy = random.choice([-1, 1]) * self.speed
            self.id = id
        
        def move(self):
            self.x += self.dx
            self.y += self.dy
            self.rect = self.image.get_rect(center=(self.x, self.y))
        
        def draw(self):
            WINDOW.blit(self.image, self.rect)
        
        def bounce(self, images):
           
            #handles the collisions and also changes the images and id of objects
            #regarding who is stronger

            for other in images:
                if other != self:
                    if self.rect.colliderect(other.rect):
                        if abs(self.dx) < abs(self.dy):
                            self.dy *= -1
                            other.dy *= -1
                        else:
                            self.dx *= -1
                            other.dx *= -1


                        if self.id == 1:
                            if other.id == 2:
                                other.image = self.image
                                other.id = self.id
                                images_count[0] += 1
                                images_count[1] -= 1

                            elif other.id == 3:
                                self.image = other.image
                                self.id = other.id
                                images_count[2] += 1
                                images_count[0] -= 1
                        
                        elif self.id == 2:
                            if other.id == 3:
                                other.image = self.image
                                other.id = self.id
                                images_count[1] += 1
                                images_count[2] -= 1
                        
                            elif other.id == 1:
                                self.image = other.image
                                self.id = other.id
                                images_count[0] += 1
                                images_count[1] -= 1

                        else:
                            if other.id == 1:
                                other.image = self.image
                                other.id = self.id
                                images_count[2] += 1
                                images_count[0] -= 1
                        
                            elif other.id == 2:
                                self.image = other.image
                                self.id = other.id
                                images_count[1] += 1
                                images_count[2] -= 1
                        
            
            # Helps to bounce off the window edges
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.dx *= -1
            if self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.dy *= -1

    #image load
    PAPER = pygame.transform.scale(pygame.image.load("media/paper.png").convert_alpha(), (VALUES[3], VALUES[3]))
    ROCK = pygame.transform.scale(pygame.image.load("media/rock.png").convert_alpha(), (VALUES[3], VALUES[3]))
    SCISSOR = pygame.transform.scale(pygame.image.load("media/scissor.png").convert_alpha(), (VALUES[3], VALUES[3]))
    
    images = []
    images_count = [VALUES[0], VALUES[1], VALUES[2]]
    
    #creation of objects paper, rock scissors
    for i in range(VALUES[0]):

        if VALUES[4] == 0:
            speed = random.randint(1, 4)
        else:
            speed = VALUES[4]

        img = Image(random.randint(50, WIDTH - 50), random.randint(50, WIDTH - 50), PAPER, speed, 1)
        images.append(img)
    
    for i in range(VALUES[1]):

        if VALUES[4] == 0:
            speed = random.randint(3, 6)
        else:
            speed = VALUES[4]

        img = Image(random.randint(50, WIDTH - 50), random.randint(50, WIDTH - 50), ROCK, speed, 2)
        images.append(img)
    
    for i in range(VALUES[2]):

        if VALUES[4] == 0:
            speed = random.randint(2, 5)
        else:
            speed = VALUES[4]

        img = Image(random.randint(50, WIDTH - 50), random.randint(50, WIDTH - 50), SCISSOR, speed, 3)
        images.append(img)
    
    #restore speed value back
    VALUES[4] = 0

    text_surface = pygame.font.Font('freesansbold.ttf', 25).render("Press Esc to Stop", True, (64, 64, 64, 0))
    text_width, text_height = text_surface.get_size()
    text_x = (WIDTH - text_width) // 2
    text_y = 900


    musicTwo = pygame.mixer.Sound('audio2.mp3')
    musicTwo.set_volume(0.1)


    while True:
        musicTwo.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN and  event.key == pygame.K_ESCAPE:
                musicTwo.stop()
                return 
        
        WINDOW.fill((100, 100, 100))
        
        # move the objects and draw them
        for img in images:
            img.move()
            img.bounce(images)
            img.draw()
        
        #text about escape button
        WINDOW.blit(text_surface, (text_x, text_y ))

        pygame.display.update()

        #if some two objects amount is zero stop the game
        #and redirect to menu page

        if(images_count[0] == 0 and images_count[1] == 0):
            musicTwo.stop()
            return 'Scissors'
        elif(images_count[1] == 0 and images_count[2] == 0):
            musicTwo.stop()
            return 'Paper'
        elif(images_count[2] == 0 and images_count[0] == 0):
            musicTwo.stop()
            return 'Rock'

     
        #limits the speed of movements, fps
        clock.tick(60)

        

        