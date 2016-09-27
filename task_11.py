#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    i=1
    while i!=0:
        if wall_is_above()==True and wall_is_beneath()==True:
            fill_cell()
            move_right(1)
        else:
            move_right(1)
        if wall_is_on_the_right()==True:
            if wall_is_above()==True and wall_is_beneath()==True:
                fill_cell()
            i=0



    pass


if __name__ == '__main__':
    run_tasks()
