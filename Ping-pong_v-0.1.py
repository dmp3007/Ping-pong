from pygame import *
font.init()
#подключить возможности текста


#создай окно игры
window = display.set_mode((800, 600))
display.set_caption('ping-pong')
background = transform.scale(image.load('tf2_wallpaper.png'), (800, 600))

#создать свою иконку в панели задач (СНИЗУ!)
icon = image.load('icon.png')  # Твоя иконка
display.set_icon(icon)



# mixer.init()
# mixer.music.load('sound_shoot.mp3') #тут вставить фоновую музыку
# #подключить музыку на фон 
# mixer.music.set_volume(0.1) #1 - макс, 0 - выкл
# #устанавливаем громкость
# mixer.music.play()
# #начать проигрывание фоновой музыки
# # kick = mixer.Sound('.ogg') #тут при проигрыше
# # money = mixer.Sound('.ogg') #тут при победе
# #загрузить звук для разового вопроизведения
# #воспроизвести звук
# fire_sound = mixer.Sound('fire.ogg')
# fire_sound.set_volume(0.1)

font_win = font.SysFont('Arial', 70)
# font_standart = font.SysFont('Arial', 30)
#установить шрифт/размер 70. Создали обьект Font с такими параметрами


class  GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wit, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wit, height))
        #
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        #прямоугольник на котором картинка = получаем ее координаты  
        self.rect.x = player_x #получаем координату х
        self.rect.y = player_y #по y соответственно
    def reset(self):
    #отрисовываем картинку в ее координатах (которые задали)
        window.blit(self.image, (self.rect.x, self.rect.y))

#делаем класс-наследник от основы, в него мы запихиваем метод с управлением

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        #прописали для первого спрайта
        # if keys_pressed[K_w] and self.rect.y > 0:
        #     self.rect.y -= self.speed
        # if keys_pressed[K_s] and self.rect.y < 400:
        #     self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
        #обработали нажатия пользователя c условием что они не выходят из поля зрения


clock = time.Clock()
FPS = 60
#задали частоту кадров
#     clock.tick(FPS) в конце также



#создали спрайты
finish = 0

game = True
while game == True:
    
    for e in event.get():
    #       список всего-всего что нажал пользователь
        if e.type == QUIT:
            game = False

           
    #ВЫХОД       1  - True
    if finish != 1:
        window.blit(background, (0, 0))
    
    
    clock.tick(FPS)
    display.update()
    #на каждом while отрисовываем заного содержимое окна
