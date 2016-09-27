#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    i=1
    while i!=0:
        if wall_is_above()==False and wall_is_beneath()==False:
            move_up(1)
            fill_cell()
            move_down(2)
            fill_cell()
            move_up(1)
        if wall_is_above()==False:
            move_up(1)
            fill_cell()
            move_down(1)
        if wall_is_beneath()==False:
                move_down(1)
                fill_cell()
                move_up(1)
        if wall_is_on_the_right()==False:
                move_right(1)
        else:
             i=0
    pass


if __name__ == '__main__':
    run_tasks()
