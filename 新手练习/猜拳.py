import random

while True:
    player = int(input('输入数字，剪刀--0，布--1，拳--2，结束程序--（-1）'))
    computer = random.randint(0, 2)
    if player == 0 or player == 1 or player == 2:
        if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or (
                (player == 2) and (computer == 0)):
            print('玩家获胜')
            print(computer)
        elif player == computer:
            print('平局')
            print(computer)
        else:
            print('电脑获胜')
            print(computer)
    elif player == -1:
        print('程序结束')
        break
    else:
        print('请按规则输入正确的数字')
