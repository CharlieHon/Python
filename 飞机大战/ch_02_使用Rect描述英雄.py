import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))  # 100 500
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height)) # 120 125
print("英雄的尺寸 %d %d" % hero_rect.size)  # 120 125
