from PyQt5.QtCore import pyqtSignal, QObject
from step import Step
from user import User
from node import Node, register_nodes

class Agent(QObject):
    ready_read_step = pyqtSignal()
    def __init__(self, viewer, monitor, controller, parent=None):
        super(Agent, self).__init__(parent)
        self.control_status = "free"

        # Register viewer, monitor and controller
        self.viewer = viewer
        self.monitor = monitor
        self.controller = controller

        self.me = None
        self.is_my_turn = False
        self.users = []

        self.steps = []
        self.my_steps = []
        self.my_last_step = -1

        # Set all the nodes on the map
        self.nodes = register_nodes(self.viewer, self.monitor)
        for node in self.nodes:
            node.set_visible(True)
        print(self.nodes)
        for node_index, node in enumerate(self.nodes):
            print(lambda: self.node_clicked(node_index))
            self.nodes[node_index].clicked.connect(self.node_clicked)
        # self.nodes[0].clicked.connect(lambda: self.test(000000))
        # self.nodes[1].clicked.connect(lambda: self.test(111111))
        self.controller.b_buy_node.clicked.connect(self.buy_node_clicked)
        self.controller.b_next_turn.clicked.connect(self.next_turn_clicked)

    def test(self, hehehe):
        print(hehehe)

    def read_new_step(self):
        print(self.my_last_step)
        self.my_last_step += 1
        return self.my_steps[self.my_last_step]

    def can_read_new_step(self):
        if (self.my_last_step+1 < len(self.my_steps)):
            return True
        else:
            return False

    # User actions
    def next_turn_clicked(self):
        step = Step()
        step.action = "next turn"
        self.my_steps.append(step)
        self.ready_read_step.emit()

    def buy_node_clicked(self):
        self.control_status = "buying node"
        self.controller.set_buying_node()
        self.monitor.set_buying_node()
        for node in self.nodes:
            if self.me.can_buy_node(node):
                print("can buy this")
                node.set_can_buy()

    def node_clicked(self, node_index):
        print(node_index)
        node = self.nodes[node_index]
        print("The node is", node)
        # If the node is clicked, either buy it or just show it
        if self.control_status == "buying node":
            if node.can_buy():
                print("here")
                step = self.me.buy_node(node)
                self.my_steps.append(step)
                self.ready_read_step.emit()
            self.controller.free()
            self.control_status = "free"

        elif self.control_status == "free":
            node.show_information()

    def escape_pressed(self):
        last_control_status = self.control_status
        self.control_status = "free"
        # Clean the buying node status
        if last_control_status == "buying node":
            for node in self.nodes:
                node.set_normal()

    # Write
    def get_last_step(self):
        if len(self.steps) == 0:
            return Step()
        return self.steps[-1]

    def is_leagal_step(self, step):
        print(step.index, self.get_last_step().index)
        if step.index <= self.get_last_step().index+1:
            return True
        else:
            return False

    def build_detector(step):
        user = step.user
        detector_number = step.command[0]
        the_detector = self.detector_list[detector_number]
        self.users[user].build_detector(the_detector)

    def build_accelerator(step):
        user = step.user
        accelerator_number = step.command[0]
        self.users[user].build_detector(accelerator_number)

    def get_funding(self, step):
        # print("Get funding")
        user = self.users[step.user]
        funding_money = step.command[0]
        user.get_funding(funding_money)
        # self.users[user].get_funding(funding_money)

    def get_extra(step):
        pass

    def get_lumionisity(step):
        pass

    def get_particle(step):
        pass

    def by_node(step):
        pass

    def destroy_detector(step):
        pass

    def destroy_accelerator(step):
        pass

    def start_game(self, step):
        self.viewer.set_background("map")

    def set_user(self, step):
        print("Agent:Setup User")
        user = User(step.command[0], step.command[1], step.user)
        print("user is", step.user, "work user is", step.work_user)
        if step.user == step.work_user:
            self.me = user
        print(step.command[2])
        user.nodes.append(self.nodes[step.command[2]])
        self.users.append(user)
        for node in user.nodes:
            node.change_owner(step.user)
        self.monitor.show_message("New user %s"%user.username)
        self.monitor.show_message("Ha Ha %s"%user.username)
        # self.viewer.draw_user(index, x, y)

    def buy_node(self, step):
        print("Buy node")
        user = self.users[step.user]
        node = self.nodes[step.command[0]]
        user.funding -= node.cost
        user.nodes.append(node)
        node.change_owner(step.user)

    def process(self, step):
        if self.me is not None and step.work_user == self.me.index:
            self.controller.checkout_my_turn(True)
        else:
            self.controller.checkout_my_turn(False)
        # Judge whether this step have been processed already
        self.steps.append(step)
        if step.action == "setup user":
            self.set_user(step)

        if step.action == "get funding":
            self.get_funding(step)

        if step.action == "start game":
            self.start_game(step)

        if step.action == "buy node":
            self.buy_node(step)
        """
        if step.index == self.get_last_step().index:
            return
        if step.index == self.get_last_step().index:
            pass
        if step.action == "build detector":
            self.build_detector()
        if step.action == "build accerator":
            self.build_accerator()
        if step.action == "get extra":
            self.get_extra()
        if step.action == "get lumionisity":
            self.get_lumionisity()
        if step.action == "get particle":
            self.get_particle()
        if step.action == "buy node":
            self.by_node()
        if step.action == "destroy detector":
            self.destroy_detector()
        if step.action == "destroy accelerator":
            pass
        """
