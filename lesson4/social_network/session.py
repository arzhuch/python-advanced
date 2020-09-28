class Session:
    class __Session:
        def __init__(self, user):
            self.user = user

        def __str__(self):
            return repr(self) + self.user

    instance = None

    def __init__(self, user):
        if not Session.instance:
            Session.instance = Session.__Session(user)
        else:
            Session.instance.user = user

    def __getattr__(self, name):
        return getattr(self.instance, name)