class WeChatMessage(object):
    pass


class TextMessage(WeChatMessage):
    def __init__(self, touser, fromuser, time, content):
        self.target = touser
        self.source = fromuser
        self.time = int(time)
        self.content = content


class ImageMessage(WeChatMessage):
    def __init__(self, touser, fromuser, time, img):
        self.target = touser
        self.source = fromuser
        self.time = int(time)
        self.img = img


class LocationMessage(WeChatMessage):
    def __init__(self, touser, fromuser, time,
                 location_x, location_y, scale, label):
        self.target = touser
        self.source = fromuser
        self.time = time
        self.location = (location_x, location_y)
        self.scale = scale
        self.label = label
