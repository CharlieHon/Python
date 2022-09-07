import pygame

pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./飞机大战/images/background.png")
screen.blit(bg, (0,0))

# 绘制英雄飞机
hero = pygame.image.load("./飞机大战/images/me1.png")
screen.blit(hero, (200, 500))

# 更新屏幕显示，可以在所有绘制工作完成之后，统一调用 update 方法
pygame.display.update()


while True:
    pass

pygame.quit()