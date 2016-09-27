#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    n=1
    while n!=0:
        if wall_is_beneath()==False:
            move_down(1)
        else:
            n=0
    i=1
    while i!=0:
        if wall_is_beneath()==True:
            move_right(1)
        else:
            i=0
    move_down(1)
    move_left(1)
    z=1
    while z!=0:
        if wall_is_above()==True:
            move_left()
            if wall_is_on_the_left()==True:
                z=0

    pass


if __name__ == '__main__':
    run_tasks()
