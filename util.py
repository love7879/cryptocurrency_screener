from os import mkdir
from os.path import isdir
from datetime import datetime


def check_directory(dir_name: str):
    if not isdir(dir_name):
        mkdir(dir_name)


def get_datetime():
    return str(datetime.now().strftime("%Y%m%d%H%M%S"))
