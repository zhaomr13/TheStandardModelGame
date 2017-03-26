class Step:
    def __init__(self):
        self.index = 0

    """

    def __init__(self, user, action, index):
        self.user = user
        self.action = action
        self.index = index
        pass
    """

class Agent():
    def __init__(self, viewer):
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

    def register_detectors(self):
        pass

    def get_last_step(self):
        if len(self.steps) == 0:
            return Step()
        return self.steps[-1]

    def is_leagal_step(self, step):
        if step.index <= self.get_last_step().index+1:
            return True

    def build_detector(step):
        user = step.user
        detector_number = step.command[0]
        the_detector = self.detector_list[detector_number]
        self.users[user].build_detector(the_detector)

    def build_accelerator(step):
        user = step.user
        accelerator_number = step.command[0]
        self.users[user].build_detector(accelerator_number)

    def get_funding(step):
        user = step.user
        funding_money = step.command[0]
        self.users[user].get_funding(funding_money)

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

    def process(self, step):
        # Judge whether this step have been processed already
        """
        if step.index == self.get_last_step().index:
            return
        if step.index == self.get_last_step().index:
            pass
        if step.action == "build detector":
            self.build_detector()
        if step.action == "build accerator":
            self.build_accerator()
        if step.action == "get funding":
            self.get_funding()
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
