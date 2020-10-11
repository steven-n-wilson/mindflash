
class card_base:
    def __init__(self, frontside, backside):
        self.frontside = frontside
        self.backside = backside

    def front(self):
        return self.frontside

    def back(self):
        return self.backside
