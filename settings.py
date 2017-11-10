#-*-coding:utf-8-*-
class Settings():
    def __init__(self):
    #初始化游戏的设置
    #屏幕设置
        self.screen_width = 800
        self.screen_height = 900
        self.bg_color = (1, 1, 1)
        self.ship_speed_factor = 1.5
    #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width =3
        self.bullet_height = 15
        self.bullet_color = 50, 50, 50
        self.bullet_allowed = 4
    #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示右移，-1表示左移
        self.fleet_direction = 1
    #飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3