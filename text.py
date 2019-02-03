import json

filename = 'username'


def get_new_user():
    """用户不存在，获取新用户"""
    username = input("What's your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def get_recorded_user():
    """获取已有的用户"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    # 当找不到文件时
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """向用户发出一条问候"""
    username = get_recorded_user()
    if username:
        print("Hello, " + username + "!")
    else:
        username = get_new_user()
        print("We will remember you next time, " +
              username + "!")


greet_user()