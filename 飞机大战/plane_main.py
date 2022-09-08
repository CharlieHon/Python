# coding=utf8
from logging import PlaceHolder
import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏类"""

    def __init__(self) -> None:
        print("游戏初始化")

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collider()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collider(self):
        pass

    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()
    

if __name__ == "__main__":

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()

