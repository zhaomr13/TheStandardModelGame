from node import Node
from step import Step

class User():
    def __init__(self, username, avatar, index, monitor):
        self.index = index
        self.username = username
        self.avatar = avatar
        self.accelerators = []
        self.nodes = []
        self.detectors = []
        self.funding = 0
        self.monitor = monitor

    def get_information(self):
        message = "Name: %s\nFunding: %d\nNodes: %d\nAccelerators: %d\nDetectors: %d\n"%(self.username, self.funding, len(self.nodes), len(self.accelerators), len(self.detectors))
        return message

    def can_buy_node(self, node):
        if node.owner is not None:
            return False
        print(node.cost, self.funding)
        if node.cost > self.funding:
            return False

        for my_node in self.nodes:
            if my_node is node:
                return False

        for my_node in self.nodes:
            if my_node.is_neighboor(node):
                return True

        return False

    def buy_node(self, node):
        # self.funding -= node.cost
        # node.change_owner(self.index)
        # self.nodes.append(node)
        step = self.my_step()
        step.action = "buy node"
        print("buy node index", node.index)
        step.command.append(node.index)
        return step

    def my_step(self):
        step = Step()
        step.user = self.index
        step.work_user = self.index
        return step

    def get_funding(self, funding_money):
        self.funding += funding_money

    def build_detector(self, the_detector, the_node):
        the_node = node_list[node_number]
        self.funding -= the_detector.cost
        self.detectors.append[detector_number]
        canvas.draw_picture_at(the_detector, the_node)


