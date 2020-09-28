from datetime import datetime
from post import Post


class User:
    _storage = []

    @staticmethod
    def get_user_by_username(usermane):
        for i in User._storage:
            if i.username == usermane:
                return i

    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.created = datetime.now()

        User._storage.append(self)

        self.posts = []

    def new_post(self, *args):
        content = input("What's up? \n")
        post = Post(self, content)
        self.posts.append(post)

    def show_recent_post(self, *args):
        try:
            last_post = self.posts[-1]
            print(f"Last time you've posted on {last_post.timestamp}:\n > {last_post.content} \n")
        except IndexError:
            pass

    def show_all_posts(self, *args):
        print(f"Your posts history:\n")
        for p in self.posts:
            print(f"\nOn {p.timestamp} you posted: \n > {p.content}")


class Admin(User):

    def show_all_users(self):

        print("Here's the list of users: \n")
        for u in User._storage:
            print(f"\nUsername: {u.username}\n"
                  f"Registered on: {u.created}\n"
                  f"Is admin?: {isinstance(u, Admin)}")

    def show_user_posts(self):
        user = User.get_user_by_username(input("Enter username: "))
        print(f"All posts  by {user.username}:\n")
        for p in user.posts:
            print(f"\nPosted on: {p.timestamp}: \n"
                  f" > {p.content}")

    def show_full_posts_history(self):

        for p in Post._storage:
            print(f"\nPosted by {p.user}: "
                  f"Posted on: {p.timestamp}: \n"
                  f" > {p.content}\n")

    def grant_admin(self):
        user = User.get_user_by_username(input("Enter username: "))
        user.__class__ = Admin
