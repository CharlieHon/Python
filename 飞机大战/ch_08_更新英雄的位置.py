import pygame

# 游戏的初始化
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

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义 rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 游戏循环 -> 意味着游戏的正式开始
while True:
    # tick()的参数指定循环体内部的代码执行的频率
    clock.tick(60)
    
    # 2.修改飞机的位置
    hero_rect.y -= 1
    # 当飞机底部超出屏幕时，飞机从主屏幕进入
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    # 3.调用 blit 方法绘制图像
    screen.blit(bg, (0,0))
    screen.blit(hero, hero_rect)
    # 4.调用 update 方法更新显示
    pygame.display.update()

pygame.quit()