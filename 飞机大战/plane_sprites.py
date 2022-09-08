# *-* coding:utf8 *-*
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 屏幕刷新率
FRAME_PER_SEC = 60

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1) -> None:
        
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        
    def update(self):

        # 在屏幕的垂直方向移动
        self.rect.y += self.speed

