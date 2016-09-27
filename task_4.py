#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_on_the_left()==True:
        if wall_is_above()==True:
            if wall_is_on_the_right() == True:
                move_down(1)
            else:
                move_right(1)
        else:
            move_up(1)
    else:
        move_left(1)


    pass


if __name__ == '__main__':
    run_tasks()
