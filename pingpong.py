from pygame import *
backcolor = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(backcolor)
sprite1 = 'ball.png'
sprite2 = 'stick.png'

clock = time.Clock()
FPS = 60 
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed 
        if keys[K_DOWN]:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed 
        if keys[K_s]:
            self.rect.y += self.speed
speed_x = 3
speed_y = 3
        
ball = GameSprite(sprite1, 300, 400, 7, 65, 65)
stick1 = Player(sprite2, 500, 200, 7, 100, 100)
stick2 = Player(sprite2, 50, 300, 7, 100, 100)

while game:
    window.fill(backcolor)
    clock.tick(FPS)
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(stick1, ball) or sprite.collide_rect(stick2, ball):
            speed_x *= -1
        stick1.update()
        stick1.reset()
        stick2.update2()
        stick2.reset()
        ball.update()
        ball.reset()
    

    
    display.update()