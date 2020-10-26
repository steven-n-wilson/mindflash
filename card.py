class card:
    def __init__(self,
                 width: float = None,
                 height: float = None,
                 color: str = None,
                 font: str = None,
                 front: str = None,
                 back: str = None,
                 media_f: str = None
                 ):
        self.color = color
        self.width = width
        self.height = height
        self.font = font
        self.front = front
        self.back = back
        self.media_f = media_f  # Media file.
        ##just a comment

    def html(self):
        pass

    def __str__(self):
        string = str()
        for k, v in self.__dict__.items():
            string += str(k) + " " + str(v) + "\n"
        return string

    # Setters.
    def set_color(self, color):
        self.color = color

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_font(self, font):
        self.font = font

    def set_front(self, front):
        self.front = front
    
    def set_back(self, back):
        self.back = back

    def set_media_f(self, media_f):
        self.media_f = media_f
    # Getters.

    def get_color(self):
        return self.color

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_font(self):
        return self.font

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def get_media_f(self):
        return self.media_f
