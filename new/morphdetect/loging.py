import datetime


def log_info(message: str):
    print(str(datetime.datetime.now()) + ": " + str(message))


def log_error(message: str):
    print(str(datetime.datetime.now()) + ": " + str(message))
