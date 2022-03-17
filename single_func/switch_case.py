# Implement Python Switch Case Statement using Dictionary

def monday():
    print('aaaaa')
    return "monday"


def tuesday():
    print('bbbbb')
    return "tuesday"


def wednesday():
    return "wednesday"


def thursday():
    return "thursday"


def friday():
    return "friday"


def saturday():
    return "saturday"


def sunday():
    return "sunday"


def default():
    return "Incorrect day"


switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }


def switch(day_of_week):
    return switcher.get(day_of_week, default)()


if __name__ == "__main__":
    print(switch(1))
    print(switch(0))
