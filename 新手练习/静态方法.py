import random


class Game(object):
    # instance = None
    score_list = []
    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #     return cls.instance

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def illustrate():  # 说明游戏规则
        print('这个游戏的规则如下...')

    @classmethod
    def show_max_score(cls):  # 获取最高分并公布最高分
        if len(cls.score_list) > 0:
            max_score = max(cls.score_list)
            print('历史最高分为%d' % max_score)
        else:
            print('还没有最高分出现')

    def start_game(self):  # 开始游戏
        score = random.randint(0, 100)  # 随机生成玩家分数
        print('玩家%s开始了游戏,获得了%d分' % (self.player_name, score))
        Game.score_list.append(score)


def main():
    Game.illustrate()
    chenliang = Game('陈亮')
    xiaoming = Game('小明')
    xiaofang = Game('小芳')
    chenliang.start_game()
    chenliang.start_game()
    xiaoming.start_game()
    xiaofang.start_game()
    Game.show_max_score()


if __name__ == '__main__':
    main()
