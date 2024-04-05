class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print(f'你扣动板机,开了一枪,当前子弹数量为{self.bullet_count}')
        else:
            print('子弹数量不够，请添加子弹')

    def add_bullet(self, count):
        self.bullet_count += count
        print(f'你装填了{count}发子弹')


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)

            return
        print("冲啊...[%s]" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun('AK47')
chenliang = Soldier('陈亮')
chenliang.gun = ak47
chenliang.fire()
