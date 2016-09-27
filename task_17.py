#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while cell_is_filled()==False:
        move_up(1)
    move_left(1)
    if cell_is_filled()==True:
        return
    else:
        move_right(2)
    pass


if __name__ == '__main__':
    run_tasks()
