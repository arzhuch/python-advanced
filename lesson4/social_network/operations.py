from time import sleep
from session import Session
from user import User, Admin


def sign_up():
    while True:
        input_username = input('Create your username: ')
        if input_username in [i.username for i in User._storage]:
            print(f"Sorry, <{input_username}> is already taken :(")
        else:
            break

    while True:
        input_password = input('Set your password: ')
        if len(input_password) < 6:
            print("Your password must have at least 6 characters!")
        else:
            break

    while True:
        try:
            age = int((input('How old are you?: ')))
        except ValueError:
            print("Age must be numeric! ")
        else:
            if age < 0:
                print("Age must be positive! ")
            else:
                break

    # the first user becomes an admin
    if not User._storage:
        user = Admin(input_username, input_password, age)
    else:
        user = User(input_username, input_password, age)
    return log_in(user)


def log_in(user=None):
    logged_in = False

    if not user:
        while True:

            while True:
                input_username = input("Enter username: ")
                if input_username not in [i.username for i in User._storage]:
                    print("The user account does not exist")
                else:
                    break

            user = User.get_user_by_username(input_username)
            i = 0
            while i < 3:
                input_password = input("Enter password: ")
                i += 1
                if input_password == user.password:
                    session = Session(user)
                    logged_in = True
                    break
                else:
                    print("\n Incorrect password \n")
            if not logged_in:
                print("Incorrect password entered 3 times, try again in 10 seconds")
                sleep(10)
            else:
                break

    else:
        session = Session(user)
    print(f"Hi, {session.user.username}!")
    return session


def startup_selector():
    start_up_actions_desc = "Welcome to Konsole, CL-based social network!\n" \
                            "\nWhat do you want to do today?\n" \
                            "1 - Sign up \n" \
                            "2 - Sign in: "

    startup_actions = {
        "1": sign_up,
        "2": log_in
    }

    while True:
        action = input(start_up_actions_desc)

        try:
            session = startup_actions[action]()
        except KeyError:
            print("Please select one of the suggested options\n")
        else:
            break
    return session


def operations_selector(session):
    user_actions_desc = "What do you want to do today? \n \n" \
                               "1 - New Post \n" \
                               "2 - Show my recent post \n" \
                               "3 - Show all my posts \n" \
                               "0 - Log out: \n"

    admin_actions_desc = "What do you want to do today? \n \n" \
                         "1 - New Post \n" \
                         "2 - Show my recent post \n" \
                         "3 - Show all my posts \n" \
                         "4 - Show list of users\n" \
                         "5 - Show user posts\n" \
                         "6 - Show full posts history\n" \
                         "7 - Grant ADMIN permissions\n" \
                         "0 - Log out"

    user = session.user

    if isinstance(user, Admin):
        operations = {
            "1": user.new_post,
            "2": user.show_recent_post,
            "3": user.show_all_posts,
            "4": user.show_all_users,
            "5": user.show_full_posts_history,
            "6": user.show_user_posts,
            "7": user.grant_admin
        }
    else:
        operations = {
            "1": user.new_post,
            "2": user.show_recent_post,
            "3": user.show_all_posts
        }

    while True:
        action = input(admin_actions_desc if isinstance(user, Admin) else user_actions_desc)
        if action == "0":
            break
        else:
            try:
                operations[action]()
            except KeyError:
                print("Please select one of the suggested options\n")
