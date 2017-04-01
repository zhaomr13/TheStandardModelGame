class Step():
    def __init__(self):
        self.work_user = -1
        self.index = 0
        self.user = -1
        self.action = ""
        self.command = []

    def to_string(self):
        message = "%(user)d@%(action)s@%(index)d@%(work_user)d"%{"user":self.user, "action":self.action, "index":self.index, "work_user":self.work_user}
        if (self.action == "setup user"):
            message += "@%(username)s@%(avatar)d@%(initnode)d\n"%{"username":self.command[0], "avatar":self.command[1], "initnode":self.command[2]}
        elif (self.action == "get funding"):
            message += "@%(funding)d\n"%{"funding":self.command[0]}
        elif (self.action == "buy node"):
            message += "@%(node)d\n"%{"node":self.command[0]}
        else:
            message += "\n"

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
        self.index = int(message[2])
        self.action = message[1]
        self.work_user = int(message[3])

        """
        setup user
        message[4]/command[0]: username
        message[5]/command[1]: user avatar
        """
        if message[1] == "setup user":
            self.command.append(message[4])
            self.command.append(int(message[5]))
            self.command.append(int(message[6]))

        """
        build_detector
        """
        if message[1] == "build detector":
            self.index = message[2]

        """
        get funding
        """
        if message[1] == "get funding":
            self.command.append(int(message[4]))

        """
        buy node
        """
        if message[1] == "buy node":
            self.command.append(int(message[4]))


    """

    def __init__(self, user, action, index):
        self.user = user
        self.action = action
        self.index = index
        pass
    """


