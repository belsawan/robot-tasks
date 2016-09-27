#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while wall_is_on_the_left()==True and wall_is_on_the_right()==True:
            move_up(1)
    while wall_is_on_the_left()==False:
            move_left(1)
            if wall_is_on_the_left()==True:
                return
    while wall_is_on_the_right()==False:
            move_right(1)

    pass


if __name__ == '__main__':
    run_tasks()
