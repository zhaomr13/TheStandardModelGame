class Step:
    def __init__(self):
        self.work_user = -1
        self.index = -1
        self.user = -1
        self.action = ""
        self.command = []

    def to_string(self):
        message = ""
        if (self.action == "set user"):
            message = "%d@set user@%d@-1\n"%(self.user, self.index)

        if (self.action == "get funding"):
            message = "%d@get funding%d@%d@%d\n"%(self.user, self.index, self.work_user, self.command[0])

        if (self.action == "next turn"):
            message = "0@next turn@0\n"


        return message

    def from_string(self, message):
        """
        String encoding
        message[0]: user
        message[1]: action
        message[2]: index
        message[3]: work_user
        message[...]: depends
        """
        message = message.split("@")
        self.user = int(message[0])
        self.action = message[1]
        self.work_user = int(message[3])

        """
        set user
        message[4]/command[0]: username
        message[5]/command[1]: user avatar
        """
        if message[1] == "set user":
            self.index = message[2]
            self.command.append(message[4])
            self.command.append(int(message[5]))

        """
        build_detector
        """
        if message[1] == "build detector":
            self.index = message[2]

        """
        get funding
        """
        if message[1] == "get funding":
            self.index = int(message[2])
            self.command.append(int(message[3]))


    """

    def __init__(self, user, action, index):
        self.user = user
        self.action = action
        self.index = index
        pass
    """

class Agent():
    def __init__(self, viewer):
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
        # print("Get funding")
        # user = step.user
        # funding_money = step.command[0]
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

    def set_user(self, step):
        user = User()
        user.name = step.command[0]
        user.avatar = step.command[1]
        users.append(user)

    def process(self, step):
        # Judge whether this step have been processed already
        if step.action == "set user":
            self.set_user(step)

        if step.action == "get funding":
            self.get_funding()
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
