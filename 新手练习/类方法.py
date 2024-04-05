class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_count(cls):
        print('工具数量为%d' % cls.count)


hatchet = Tool('斧头')
hoe = Tool('锄头')
bucket = Tool('水桶')
Tool.show_count()
