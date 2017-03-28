class User():
    def __init__(self, username, avatar, index):
        self.index = index
        self.username = username
        self.avatar = avatar
        self.accelerators = []
        self.nodes = []
        self.detectors = []
        self.funding = 0

    def get_funding(self, funding_money):
        self.funding += funding_money

    def build_detector(self, the_detector, the_node):
        the_node = node_list[node_number]
        self.funding -= the_detector.cost
        self.detectors.append[detector_number]
        canvas.draw_picture_at(the_detector, the_node)


