import datetime
from uuid import uuid4


class Post:

    _storage = []

    def __init__(self, user, content='Empty post'):
        self.post_id = uuid4()
        self.user = user.username
        self.timestamp = datetime.datetime.now()
        self.content = content

        Post._storage.append(self)

    def show_post(self, *args):
        print(f'Posted by {self.user.first_name} {self.user.last_name} on {self.timestamp}: \n')
        print(self.content)
