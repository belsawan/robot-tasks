#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    i=1
    while i!=0:
        if wall_is_above()==False and wall_is_beneath()==True:
            fill_cell()
        if wall_is_on_the_right()==True:
            i=0
        else:
            move_right(1)
    pass


if __name__ == '__main__':
    run_tasks()
z