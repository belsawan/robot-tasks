#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    if wall_is_on_the_right()==True:
       move_left(1)
    else:
       move_right(1)
    if wall_is_above()==False:
        move_up(1)
    else:
        while wall_is_above()==True and wall_is_on_the_left()==False:
                move_left(1)
                if wall_is_on_the_left()==True:
                    while wall_is_on_the_right()==False and wall_is_above()==True:
                         move_right(1)
    if wall_is_above()==False:
        while wall_is_above()==False:
            move_up(1)
        while wall_is_on_the_left()==False:
            move_left(1)


    pass


if __name__ == '__main__':
    run_tasks()
