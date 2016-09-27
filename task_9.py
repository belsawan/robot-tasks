#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    i=1
    while i!=0:
        if wall_is_beneath()==True and wall_is_above()==True:
            move_right(1)
        if wall_is_above()==False:
            fill_cell()
        if wall_is_on_the_right()==False:
            move_right(1)
        else:
            i=0
    pass


if __name__ == '__main__':
    run_tasks()
