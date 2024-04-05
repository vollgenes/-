class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '家具:%s, 面积:%.2f' % (self.name, self.area)


class House:
    def __init__(self, area, house_type):
        self.area = area
        self.house_type = house_type
        self.free_area = area
        self.furniture_item = []

    def __str__(self):
        return ('户型:%s\n房屋面积:%.2f\n剩余面积:%.2f\n家具列表:%s'
                % (self.house_type, self.area, self.free_area, self.furniture_item))

    def add_furniture(self, furniture):
        if self.free_area < furniture.area:
            print('面积不足')
            return
        self.furniture_item.append(furniture.name)
        self.free_area -= furniture.area


sofa = Furniture('沙发', 5)
table = Furniture('桌子', 2)
bed = Furniture('床', 3)
my_home = House(50, '两室一厅')
my_home.add_furniture(sofa)
my_home.add_furniture(table)
my_home.add_furniture(bed)
print(my_home)
