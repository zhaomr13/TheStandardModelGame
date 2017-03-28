from step import Step
from user import User

class Agent():
    def __init__(self, viewer, monitor):
        self.monitor = monitor
        self.me = None
        self.steps = []
        self.this_user = 0
        self.users = []
        self.viewer = viewer

        self.register_viewer(viewer)
        # self.register_
        # self.register_detectors()
        # self.register_notes()

        pass

    def register_viewer(self, viewer):
        self.viewer = viewer

    def register_nodes(self):
        pass


    def register_detectors(self):
        pass

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
        uesr.get_funding(funding_money)
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

    def game_start(self, step):
        self.viewer.change_background("map")

    def set_user(self, step):
        user = User(step.command[0], step.command[1], step.user)
        self.users.append(user)
        for node in user.nodes:
            node.change_user(index)
        # self.viewer.draw_user(index, x, y)

    def process(self, step):
        # Judge whether this step have been processed already
        self.steps.append(step)
        if step.action == "setup user":
            self.set_user(step)

        if step.action == "get funding":
            self.get_funding()

        if step.action == "start game":
            self.start_game(step)
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
